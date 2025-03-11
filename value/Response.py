from dataclasses import dataclass
from typing import List

from typing_extensions import TypeVar, Generic


@dataclass
class WantedStatValue:
    tag: str
    count: int

D = TypeVar('D')

@dataclass
class TimestampValue(Generic[D]):
    timestamp: int
    data: List[D]