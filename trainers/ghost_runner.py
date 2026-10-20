"""Bootstrap entry point for the ghost pipeline."""
from __future__ import annotations

import argparse
import logging
import time

from trainers.pipeline import Pipeline
from trainers.config_loader import load_config
from trainers.services.process_service import ProcessService
from trainers.services.memory_service import MemoryService


def build_pipeline(cfg: dict) -> Pipeline:
    proc = ProcessService(cfg["game"]["process_name"])
    mem = MemoryService(proc, cfg["memory"])
    pipe = Pipeline(cfg, mem)
    pipe.load_stages(cfg["pipeline"]["stages"])
    return pipe


def main() -> int:
    ap = argparse.ArgumentParser(prog="ghost_runner")
    ap.add_argument("--config", default="config/default.yaml")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_config(args.config)
    logging.basicConfig(
        level=cfg["logging"]["level"],
        filename=cfg["logging"]["file"],
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    pipe = build_pipeline(cfg)
    if args.dry_run:
        logging.info("dry-run: %d stages loaded", len(pipe.stages))
        return 0

    tick = cfg["pipeline"]["tick_ms"] / 1000.0
    try:
        while True:
            pipe.tick()
            time.sleep(tick)
    except KeyboardInterrupt:
        logging.info("shutdown requested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())