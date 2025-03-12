import json
from dataclasses import asdict
from typing import List

import pandas as pd

from infra.Local import SkillLocal, CategoryLocal, ResultLocal
from model.Results import Results

base_path = './save/'


def show():
    # print('SkillLocal')
    # print([i[0] for i in SkillLocal.load()])
    # print()
    #
    # print('CategoryLocal')
    # print([i[0] for i in CategoryLocal.load()])
    # print()
    data = []

    result: List[(int, Results)] = ResultLocal.load()
    for v in result[0][1].data:
        row = {
            'reward_total': v.reward_total,
            'is_bookmark': v.is_bookmark,
            'company': v.company,
            'title_img': v.title_img,
            'address': v.address,
            'position': v.position,
            'category_tag': v.category_tag,
            'attraction_tags': v.attraction_tags,
            'skill_tags': v.skill_tags,
            'user_oriented_tags': v.user_oriented_tags,
            'annual_from': v.annual_from,
            'annual_to': v.annual_to,
            'is_newbie': v.is_newbie,
            'reward': v.reward
        }
        data.append(row)

    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False, engine='openpyxl')

