import json
from dataclasses import asdict

from infra.Local import SkillLocal, CategoryLocal, ResultLocal

base_path = './save/'


def show():
    # print('SkillLocal')
    # print([i[0] for i in SkillLocal.load()])
    # print()
    #
    # print('CategoryLocal')
    # print([i[0] for i in CategoryLocal.load()])
    # print()

    print('ResultLocal')
    result = ResultLocal.load()
    # print([i[0] for i in ResultLocal.load()])
    print()