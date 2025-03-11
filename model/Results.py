from dataclasses import dataclass
from typing import List

from model.Result import Result
from model.Links import Links


@dataclass
class Results:
    data: List[Result]
    links: Links