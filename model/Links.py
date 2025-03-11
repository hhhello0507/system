from dataclasses import dataclass
from typing import Optional


@dataclass
class Links:
    prev: Optional[str]
    next: Optional[str]
