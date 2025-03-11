from dataclasses import dataclass
from typing import List

from model.Address import Address
from model.CategoryTag import CategoryTag
from model.Company import Company
from model.Reward import Reward
from model.TitleImg import TitleImg


@dataclass
class Result:
    id: int
    reward_total: str
    is_bookmark: bool
    company: Company
    title_img: TitleImg
    address: Address
    position: str # 직군
    category_tag: CategoryTag
    attraction_tags: List[int] # 매력 태그
    skill_tags: List[int] # 기술 태그
    user_oriented_tags: List[int] # 유저 지향 태그
    annual_from: int # 연봉 하한
    annual_to: int # 연봉 상한
    is_newbie: bool # 신입 여부
    reward: Reward