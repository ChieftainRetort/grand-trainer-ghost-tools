"""Toggle trainer flags (no-ghost, ghost-see, etc.) in memory."""
from __future__ import annotations

import logging

log = logging.getLogger(__name__)

FLAG_NO_GHOST = 0x01
FLAG_SEE_GHOST = 0x02
FLAG_FREEZE_SPIRIT = 0x04


class TrainerFlagProcessor:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory
        self.enabled = set(cfg.get("trainer", {}).get("flags", []))

    def _compose(self) -> int:
        bits = 0
        if "no_ghost" in self.enabled:
            bits |= FLAG_NO_GHOST
        if "see_ghost" in self.enabled:
            bits |= FLAG_SEE_GHOST
        if "freeze_spirit" in self.enabled:
            bits |= FLAG_FREEZE_SPIRIT
        return bits

    def run(self, payload: dict) -> dict:
        addr = payload.get("trainer_ptr_addr")
        if addr is None:
            return payload
        try:
            self.memory.write_int(addr, self._compose())
        except Exception:
            log.exception("trainer flag write failed")
            return payload
        return {**payload, "trainer_flags": sorted(self.enabled)}