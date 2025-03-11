from dataclasses import dataclass

from model.ApplicationResponseStats import ApplicationResponseStats


@dataclass
class Company:
    id: int
    name: str
    application_response_stats: ApplicationResponseStats