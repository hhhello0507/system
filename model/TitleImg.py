from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class TitleImg:
    origin: str
    thumb: str
    video: Optional[Any]