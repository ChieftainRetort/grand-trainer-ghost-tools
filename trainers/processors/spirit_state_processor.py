"""Read spirit/ghost state from memory and normalize it."""
from __future__ import annotations

import logging

log = logging.getLogger(__name__)

SPIRIT_STATES = {0: "dormant", 1: "manifested", 2: "banished", 3: "attached"}


class SpiritStateProcessor:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory

    def run(self, payload: dict) -> dict:
        addr = payload.get("ghost_flag_addr")
        if addr is None:
            return payload
        try:
            raw = self.memory.read_int(addr)
        except Exception:
            log.exception("failed to read spirit state")
            return payload
        state = SPIRIT_STATES.get(raw & 0xFF, "unknown")
        return {**payload, "spirit_state": state, "spirit_raw": raw}