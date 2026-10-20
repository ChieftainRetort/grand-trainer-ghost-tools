"""Data model for a ghost entity observed in the Grand Trainer."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GhostEntity:
    entity_id: int
    name: str
    is_ghost: bool = True
    spirit_state: str = "dormant"
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "is_ghost": self.is_ghost,
            "spirit_state": self.spirit_state,
            "position": list(self.position),
            "tags": list(self.tags),
        }