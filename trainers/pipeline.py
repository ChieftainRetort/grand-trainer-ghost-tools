"""Ordered worker pipeline: handlers -> processors -> drivers."""
from __future__ import annotations

import importlib
import logging
from typing import Any

log = logging.getLogger(__name__)


class Pipeline:
    def __init__(self, cfg: dict, memory: Any) -> None:
        self.cfg = cfg
        self.memory = memory
        self.stages: list[Any] = []
        self.state: dict[str, Any] = {}

    def load_stages(self, dotted_paths: list[str]) -> None:
        for path in dotted_paths:
            module_name, _, cls_name = path.rpartition(".")
            module = importlib.import_module(module_name)
            cls = getattr(module, cls_name.split(".")[-1])
            stage = cls(self.cfg, self.memory)
            self.stages.append(stage)
            log.info("loaded stage %s", path)

    def tick(self) -> None:
        payload: dict[str, Any] = dict(self.state)
        for stage in self.stages:
            try:
                payload = stage.run(payload) or payload
            except Exception:
                log.exception("stage %s failed", stage.__class__.__name__)
                return
        self.state = payload