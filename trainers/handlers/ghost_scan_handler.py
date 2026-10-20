"""Locate ghost flag and trainer pointer via pattern scan."""
from __future__ import annotations

import logging

log = logging.getLogger(__name__)


class GhostScanHandler:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory

    def run(self, payload: dict) -> dict:
        ghost_addr = self.memory.scan(self.cfg["memory"]["pattern_ghost_flag"])
        trainer_addr = self.memory.scan(self.cfg["memory"]["pattern_trainer_ptr"])
        if ghost_addr is None:
            log.debug("ghost flag pattern not resolved")
        if trainer_addr is None:
            log.debug("trainer pointer pattern not resolved")
        return {
            **payload,
            "ghost_flag_addr": ghost_addr,
            "trainer_ptr_addr": trainer_addr,
        }