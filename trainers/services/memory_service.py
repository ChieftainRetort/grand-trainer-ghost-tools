"""Pattern scanning and read/write helpers over the target module."""
from __future__ import annotations

import logging
import re

import pymem

log = logging.getLogger(__name__)


def _parse_pattern(pattern: str) -> tuple[bytes, bytes]:
    mask_chars = []
    raw = []
    for token in pattern.split():
        if token == "??":
            raw.append(0)
            mask_chars.append("?")
        else:
            raw.append(int(token, 16))
            mask_chars.append("x")
    return bytes(raw), "".join(mask_chars).encode()


class MemoryService:
    def __init__(self, process_service, cfg: dict) -> None:
        self.proc_service = process_service
        self.cfg = cfg
        self.pm: pymem.Pymem | None = None

    def ensure_attached(self) -> None:
        if self.pm is not None:
            return
        pid = self.proc_service.attach()
        if pid is None:
            raise RuntimeError("cannot attach to target process")
        self.pm = pymem.Pymem(pid)

    def scan(self, pattern: str) -> int | None:
        self.ensure_attached()
        needle, mask = _parse_pattern(pattern)
        regex = re.escape(needle).replace(b"\\x00", b".")
        base, size = self.cfg["scan_region"]
        try:
            region = self.pm.read_bytes(base, size - base)
        except Exception:
            log.exception("scan region read failed")
            return None
        m = re.search(regex, region)
        return base + m.start() if m else None

    def read_int(self, addr: int) -> int:
        self.ensure_attached()
        return self.pm.read_int(addr)

    def write_int(self, addr: int, value: int) -> None:
        self.ensure_attached()
        self.pm.write_int(addr, value)