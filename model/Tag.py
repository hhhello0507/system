from dataclasses import dataclass
from typing import Optional

from model.Category import Counts


@dataclass
class Tag:
    id: int
    image: Optional[str]
    title: str
    counts: Counts