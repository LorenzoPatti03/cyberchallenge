#!/usr/bin/env python3
"""Tiny brute-force scaffold for flags, passwords and tokens."""

from __future__ import annotations

import itertools


# Alfabeto base che copre la maggior parte delle flag CTF.
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-_."


def candidate_stream(prefix: str = "", max_len: int = 8):
    """Genera stringhe candidate partendo da un prefisso noto."""
    for length in range(len(prefix), max_len + 1):
        for suffix in itertools.product(ALPHABET, repeat=length - len(prefix)):
            yield prefix + "".join(suffix)


def test_candidate(candidate: str) -> bool:
    """Sostituisci questo stub con il controllo della tua challenge."""
    return False


def main() -> None:
    # Riduci max_len quando colleghi il tuo check reale.
    for candidate in candidate_stream(max_len=4):
        if test_candidate(candidate):
            print(candidate)
            break


if __name__ == "__main__":
    main()

# Uso: personalizza `test_candidate` e avvia `python bruteforce_candidate_runner.py`.
