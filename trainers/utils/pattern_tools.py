"""Helpers for building and validating memory scan patterns."""
from __future__ import annotations


def normalize_pattern(pattern: str) -> str:
    tokens = pattern.strip().upper().split()
    for t in tokens:
        if t != "??" and len(t) != 2:
            raise ValueError(f"invalid token: {t}")
    return " ".join(tokens)


def pattern_to_bytes(pattern: str) -> bytes:
    out = bytearray()
    for t in normalize_pattern(pattern).split():
        out.append(0 if t == "??" else int(t, 16))
    return bytes(out)


def pattern_offsets(pattern: str, needle: bytes) -> list[int]:
    data = pattern_to_bytes(pattern)
    hits = []
    start = 0
    while True:
        i = data.find(needle, start)
        if i < 0:
            break
        hits.append(i)
        start = i + 1
    return hits