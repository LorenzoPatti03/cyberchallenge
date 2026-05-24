#!/usr/bin/env python3
"""XOR helper and tiny brute-force scaffold for crypto challenges."""

from __future__ import annotations

from itertools import cycle


def xor_bytes(left: bytes, right: bytes) -> bytes:
    """XOR byte-a-byte su due buffer della stessa lunghezza."""
    return bytes(a ^ b for a, b in zip(left, right))


def xor_with_key(data: bytes, key: bytes) -> bytes:
    """XOR ripetendo la chiave su tutto il payload."""
    return bytes(value ^ key_byte for value, key_byte in zip(data, cycle(key)))


def score_plaintext(candidate: bytes) -> int:
    """Punteggio grezzo: preferisce testo leggibile e formati CTF comuni."""
    readable = b" etaoinshrdluETAOINSHRDLU{}_-:,.'\"/0123456789"
    return sum(byte in readable for byte in candidate)


def brute_force_single_byte(ciphertext: bytes) -> tuple[int, bytes]:
    """Trova la chiave a un byte che produce il testo piu plausibile."""
    best_key = 0
    best_plain = b""
    best_score = -1
    for key in range(256):
        plain = bytes(byte ^ key for byte in ciphertext)
        current_score = score_plaintext(plain)
        if current_score > best_score:
            best_key = key
            best_plain = plain
            best_score = current_score
    return best_key, best_plain


if __name__ == "__main__":
    # Dato di esempio per vedere il flusso di lavoro del solver.
    sample = bytes.fromhex("1b00060a")
    key, plain = brute_force_single_byte(sample)
    print(f"key={key:02x}")
    print(plain)

# Uso: importa le funzioni nel solver della challenge oppure esegui il file per il test rapido incluso.
