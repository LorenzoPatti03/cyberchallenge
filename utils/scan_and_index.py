#!/usr/bin/env python3
"""Scan the workspace and build a readable catalog under utils/index."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_EXTENSIONS = {".txt", ".md"}
PYTHON_EXTENSIONS = {".py"}
IGNORED_PARTS = {".git", "__pycache__", "node_modules", ".venv", "venv"}

EXPLANATION_HINTS = (
    "analisi",
    "spiegazione",
    "exploit",
    "attack",
    "vulnerabil",
    "oracle",
    "padding",
    "symlink",
    "argument injection",
    "zip",
    "xss",
    "ssrf",
    "rsa",
    "xor",
    "decrypt",
)

TEMPLATE_HINTS = (
    "template",
    "pwntools",
    "pwn import",
    "from pwn",
    "bruteforce",
    "brute force",
    "solver",
    "requests",
    "zipfile",
    "argparse",
)


@dataclass(frozen=True)
class CopiedFile:
    source: str
    destination: str
    category: str
    title: str


def slugify(text: str, fallback: str) -> str:
    candidate = text.strip().lower()
    candidate = re.sub(r"^[#=\-\s]+", "", candidate)
    candidate = re.sub(r"[^a-z0-9]+", "_", candidate)
    candidate = re.sub(r"_+", "_", candidate).strip("_")
    return candidate or fallback


def shorten_slug(text: str, limit: int = 80) -> str:
    if len(text) <= limit:
        return text
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    trimmed = text[: limit - 11].rstrip("_")
    return f"{trimmed}_{digest}"


def first_useful_line(content: str) -> str:
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("#", "==", "--")):
            cleaned = line.lstrip("#=- ").strip()
            if cleaned:
                return cleaned
        return line
    return ""


def classify_text(path: Path, content: str) -> str | None:
    lower = content.lower()
    if path.suffix in TEXT_EXTENSIONS:
        if any(hint in lower for hint in EXPLANATION_HINTS):
            return "explanations"
        if lower.startswith(("analisi", "template", "notes", "spiegazione")):
            return "explanations"
    if path.suffix in PYTHON_EXTENSIONS:
        if any(hint in lower for hint in TEMPLATE_HINTS):
            return "templates"
        if "pwninit --template-path" in lower:
            return "templates"
    return None


def build_target_name(relative_path: Path, content: str, category: str) -> str:
    parent_slug = slugify("_".join(relative_path.parts[:-1]), "root")
    stem = slugify(relative_path.stem, "file")
    title = first_useful_line(content)
    if title:
        title_slug = slugify(title, stem)
        if title_slug != stem:
            stem = f"{stem}_{title_slug}"
    suffix = relative_path.suffix
    if category == "templates" and suffix != ".py":
        suffix = ".py"
    name = f"{parent_slug}_{stem}{suffix}" if parent_slug != "root" else f"{stem}{suffix}"
    return shorten_slug(name)


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


def iter_candidate_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        if path.suffix in TEXT_EXTENSIONS | PYTHON_EXTENSIONS:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a readable catalog in utils/index.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Workspace root to scan")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "index", help="Catalog output directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing copies")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output.resolve()
    explanations_dir = output / "explanations"
    templates_dir = output / "templates"
    output.mkdir(parents=True, exist_ok=True)
    explanations_dir.mkdir(parents=True, exist_ok=True)
    templates_dir.mkdir(parents=True, exist_ok=True)

    entries: list[CopiedFile] = []
    for path in iter_candidate_files(root):
        if output in path.parents:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        category = classify_text(path, content)
        if not category:
            continue

        relative_path = path.relative_to(root)
        target_name = build_target_name(relative_path, content, category)
        destination_dir = explanations_dir if category == "explanations" else templates_dir
        destination = destination_dir / target_name

        try:
            exists = destination.exists()
        except OSError:
            exists = False

        if not exists or args.force:
            shutil.copy2(path, destination)

        entries.append(
            CopiedFile(
                source=str(path),
                destination=str(destination),
                category=category,
                title=first_useful_line(content) or path.stem,
            )
        )

    manifest = {
        "root": str(root),
        "output": str(output),
        "items": [asdict(entry) for entry in entries],
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Copied {len(entries)} files into {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
