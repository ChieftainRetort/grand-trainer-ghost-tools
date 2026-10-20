"""Attach to and inspect the Grand Trainer process."""
from __future__ import annotations

import logging

import psutil

log = logging.getLogger(__name__)


class ProcessService:
    def __init__(self, process_name: str) -> None:
        self.process_name = process_name
        self.pid: int | None = None

    def attach(self) -> int | None:
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info["name"] == self.process_name:
                self.pid = proc.info["pid"]
                log.info("attached to %s (pid=%s)", self.process_name, self.pid)
                return self.pid
        log.warning("process %s not found", self.process_name)
        return None

    def is_alive(self) -> bool:
        if self.pid is None:
            return False
        return psutil.pid_exists(self.pid)