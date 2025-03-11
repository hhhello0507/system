from dataclasses import dataclass
from typing import List
from model.Skill import Skill


@dataclass
class Skills:
    skill: List[Skill]

    def to_dict(self) -> dict[int, str]:
        return {s.id: s.text for s in self.skill}