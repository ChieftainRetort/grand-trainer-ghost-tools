"""Filter entity list down to ghost-tagged actors."""
from __future__ import annotations

import logging

log = logging.getLogger(__name__)


class EntityGhostFilter:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory

    def run(self, payload: dict) -> dict:
        entities = payload.get("entities", [])
        ghosts = [e for e in entities if e.get("is_ghost")]
        return {**payload, "ghost_entities": ghosts, "ghost_count": len(ghosts)}