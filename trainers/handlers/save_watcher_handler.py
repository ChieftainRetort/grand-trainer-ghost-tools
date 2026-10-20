"""Watch the local save file for changes and enqueue reloads."""
from __future__ import annotations

import logging
import time
from pathlib import Path

log = logging.getLogger(__name__)


class SaveWatcherHandler:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory
        self._save_path = Path(cfg.get("save", {}).get("path", "saves/slot0.sav"))
        self._last_mtime = 0.0

    def run(self, payload: dict) -> dict:
        if not self._save_path.exists():
            return payload
        mtime = self._save_path.stat().st_mtime
        if mtime > self._last_mtime:
            self._last_mtime = mtime
            log.info("save file changed: %s", self._save_path)
            return {**payload, "save_reload": True}
        return payload