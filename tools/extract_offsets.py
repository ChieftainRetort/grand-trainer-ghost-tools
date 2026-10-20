"""Standalone helper to dump offsets from a live GrandTrainer.exe."""
from __future__ import annotations

import argparse
import json

from trainers.config_loader import load_config
from trainers.services.process_service import ProcessService
from trainers.services.memory_service import MemoryService


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/default.yaml")
    args = ap.parse_args()
    cfg = load_config(args.config)
    proc = ProcessService(cfg["game"]["process_name"])
    mem = MemoryService(proc, cfg["memory"])
    out = {
        "ghost_flag": mem.scan(cfg["memory"]["pattern_ghost_flag"]),
        "trainer_ptr": mem.scan(cfg["memory"]["pattern_trainer_ptr"]),
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())