"""Print pipeline state to the console each tick."""
from __future__ import annotations

from rich.console import Console

NAME = "console"


class ConsoleDriver:
    def __init__(self, cfg: dict, memory) -> None:
        self.cfg = cfg
        self.memory = memory
        self.console = Console()

    def run(self, payload: dict) -> dict:
        state = payload.get("spirit_state", "n/a")
        flags = payload.get("trainer_flags", [])
        ghosts = payload.get("ghost_count", 0)
        self.console.print(
            f"[bold]spirit[/bold]={state}  "
            f"[bold]flags[/bold]={','.join(flags) or '-'}  "
            f"[bold]ghosts[/bold]={ghosts}"
        )
        return payload

    def emit(self, payload: dict) -> None:
        self.run(payload)