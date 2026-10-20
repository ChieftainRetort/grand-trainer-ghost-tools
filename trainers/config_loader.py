"""YAML config loader with defaults merge."""
from __future__ import annotations

import copy
from pathlib import Path

import yaml

DEFAULTS = {
    "pipeline": {"tick_ms": 250, "stages": []},
    "logging": {"level": "INFO", "file": "logs/ghost_runner.log"},
}


def _deep_merge(base: dict, override: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def load_config(path: str | Path) -> dict:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    return _deep_merge(DEFAULTS, raw)