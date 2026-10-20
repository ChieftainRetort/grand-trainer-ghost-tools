from trainers.utils.pattern_tools import (
    normalize_pattern,
    pattern_to_bytes,
    pattern_offsets,
)


def test_normalize_lowercase():
    assert normalize_pattern("48 8b 05 ??") == "48 8B 05 ??"


def test_pattern_to_bytes():
    assert pattern_to_bytes("48 8B ??") == b"\x48\x8b\x00"


def test_offsets_finds_multiple():
    pat = "48 8B 05 48 8B 05"
    needle = b"\x48\x8b\x05"
    assert pattern_offsets(pat, needle) == [0, 3]