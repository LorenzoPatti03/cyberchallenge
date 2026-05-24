#!/usr/bin/env python3
"""Unwrap nested encodings such as gzip, xz and base64."""

from __future__ import annotations

import base64
import gzip
import lzma
import re
from pathlib import Path


def maybe_base64(data: bytes) -> bytes | None:
    """Riconosce un blocco base64 puro anche se ha spazi o newline."""
    text = data.decode("latin1", errors="ignore")
    compact = "".join(ch for ch in text if ch not in " \r\n\t")
    if len(compact) < 32:
        return None
    if not re.fullmatch(r"[A-Za-z0-9+/=]+", compact):
        return None
    try:
        return base64.b64decode(compact)
    except Exception:
        return None


def unwrap_once(data: bytes) -> bytes:
    """Tenta un solo livello di decompressione o decodifica."""
    if data.startswith(b"\x1f\x8b"):
        # Magic bytes gzip.
        return gzip.decompress(data)
    if data.startswith(b"\xfd7zXZ\x00"):
        # Magic bytes xz.
        return lzma.decompress(data)
    decoded = maybe_base64(data)
    if decoded is not None:
        return decoded
    return data


def main(path: str) -> None:
    blob = Path(path).read_bytes()
    for _ in range(10):
        next_blob = unwrap_once(blob)
        if next_blob == blob:
            break
        blob = next_blob
    print(blob[:500].decode("latin1", errors="replace"))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} <file>")
    main(sys.argv[1])

# Uso: sostituisci il file di input e avvia `python archive_encoding_unwrapper.py <file>`.
