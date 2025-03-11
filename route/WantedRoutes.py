from collections import Counter
from typing import List, Tuple

from fastapi import APIRouter

from infra.Local import ResultLocal, SkillLocal
from model.Result import Result
from model.Results import Results
from value.Response import WantedStatValue, TimestampValue

wanted_router = APIRouter(prefix="/wanted", tags=['Wanted'])

@wanted_router.get('/all')
def fetch_wanted_stats() -> List[TimestampValue[List[WantedStatValue]]]:
    data: List[Tuple[int, Results]] = ResultLocal.load()

    result: List[TimestampValue[List[WantedStatValue]]] = []

    for value in data:
        result.append(
            TimestampValue(
                timestamp=value[0],
                data=results_to_stats(value[1])
            )
        )

    return result


@wanted_router.get('/')
def fetch_current_wanted_stat() -> List[WantedStatValue]:
    results: Results = ResultLocal.load_recent()
    return results_to_stats(results)


def results_to_stats(results: Results) -> List[WantedStatValue]:
    results: List[Result] = results.data
    skills = SkillLocal.load_recent()
    skills_dict = skills.to_dict()

    all_tags: List[str] = []

    for result in results:
        tags: List[int] = result.skill_tags
        str_tags: List[str] = [skills_dict[tag] for tag in tags if tag in skills_dict.keys()]
        str_tags = [tag.replace('.js', '').replace('.JS', '') for tag in str_tags]
        all_tags.extend(str_tags)

    all_skills_most_common = Counter(all_tags).most_common()

    r = [WantedStatValue(tag=tag, count=count) for (tag, count) in all_skills_most_common]

    return r
