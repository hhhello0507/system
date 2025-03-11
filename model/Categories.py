from dataclasses import dataclass
from typing import List
from model.Category import Category


@dataclass
class Categories:
    category: List[Category]