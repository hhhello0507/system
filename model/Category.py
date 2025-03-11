from dataclasses import dataclass
from typing import List, Optional

from model.Counts import Counts
from model.Tag import Tag

@dataclass
class Category:
    id: int
    image: str
    tags: List[Tag]
    title: str
    counts: Counts