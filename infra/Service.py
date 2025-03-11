from dataclasses import fields
from typing import Optional, List

import requests

from model.Skills import Skills
from model.Results import Results
from model.Categories import Categories

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})


def fetch_categories() -> Categories:
    response = session.get("https://static.wanted.co.kr/tags?tags=category")

    validate_response(response)

    return from_dict(Categories, response.json())


def fetch_skills() -> Skills:
    response = session.get("https://static.wanted.co.kr/tags?tags=skill")

    validate_response(response)

    return from_dict(Skills, response.json())


# 예시 사용법
# result = fetch_results(
#     job_group_id=518,
#     job_ids=[677, 678],
#     years=[0, 5],
#     limit=20
# )
def fetch_results(
        job_group_id: int,
        job_ids: Optional[List[int]] = None,
        country="kr",
        job_sort="job.latest_order",
        years: Optional[List[int]] = None,
        locations="all",
        limit=20
) -> Results:
    base_url = 'https://www.wanted.co.kr/api/chaos/navigation/v1/results'
    params = {
        'job_group_id': job_group_id,
        'country': country,
        'job_sort': job_sort,
        'locations': locations,
        'limit': limit
    }

    if job_ids:
        for i, job_id in enumerate(job_ids):
            params[f'job_ids[{i}]'] = job_id

    if years:
        for year in years:
            params[f'years'] = year

    response = session.get(base_url, params=params)

    validate_response(response)

    return from_dict(Results, response.json())


def from_dict(data_class, data):
    """
    A helper function to map the dictionary to the dataclass fields.
    """
    if not isinstance(data, dict):
        return data_class()
    # print(data_class)
    fieldtypes = {f.name: f.type for f in fields(data_class)}
    kwargs = {}
    for field, field_type in fieldtypes.items():
        value = data.get(field, None)
        if isinstance(value, dict):
            kwargs[field] = from_dict(field_type, value)  # Recursively handle nested dicts
        elif isinstance(value, list):
            # Handle lists of dicts
            kwargs[field] = [from_dict(field_type.__args__[0], item) if isinstance(item, dict) else item for item in
                             value]
        else:
            kwargs[field] = value
    return data_class(**kwargs)


def validate_response(response):
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
