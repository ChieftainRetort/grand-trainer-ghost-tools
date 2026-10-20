"""Simple bounded job queue used between pipeline stages."""
from __future__ import annotations

import queue
from dataclasses import dataclass
from typing import Any


@dataclass
class Job:
    stage: str
    payload: dict[str, Any]


class JobQueue:
    def __init__(self, maxsize: int = 256) -> None:
        self._q: queue.Queue[Job] = queue.Queue(maxsize=maxsize)

    def put(self, job: Job) -> bool:
        try:
            self._q.put_nowait(job)
            return True
        except queue.Full:
            return False

    def get(self, timeout: float = 0.1) -> Job | None:
        try:
            return self._q.get(timeout=timeout)
        except queue.Empty:
            return None

    def __len__(self) -> int:
        return self._q.qsize()