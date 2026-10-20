"""Lightweight overlay window for the Grand Trainer ghost HUD."""
from __future__ import annotations

import logging

NAME = "overlay"

log = logging.getLogger(__name__)


class OverlayDriver:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory
        self.enabled = cfg.get("overlay", {}).get("enabled", False)

    def run(self, payload: dict) -> dict:
        if not self.enabled:
            return payload
        state = payload.get("spirit_state", "dormant")
        flags = payload.get("trainer_flags", [])
        log.debug("overlay: %s | %s", state, flags)
        return payload

    def emit(self, payload: dict) -> None:
        self.run(payload)