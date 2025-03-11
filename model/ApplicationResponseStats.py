from dataclasses import dataclass


@dataclass
class ApplicationResponseStats:
    avg_rate: float
    level: str