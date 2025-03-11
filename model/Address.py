from dataclasses import dataclass


@dataclass
class Address:
    country: str
    location: str
    district: str
