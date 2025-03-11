from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Reward:
    id: Optional[Any]
    wd_id: Optional[Any]
    country: str
    user_country: str
    reward_recommender: int
    reward_recommendee: int
    reward_recommender_unit: str
    reward_recommendee_unit: str
    formatted_total: str
    formatted_recommender: str
    formatted_recommendee: str