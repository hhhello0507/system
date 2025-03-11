from apscheduler.schedulers.background import BackgroundScheduler

from infra import Service
from infra.Local import CategoryLocal, SkillLocal, ResultLocal


def scheduled_save_wanted():
    print("Fetching daily results and storing in cache...")

    categories = Service.fetch_categories()
    CategoryLocal.push(categories)

    skills = Service.fetch_skills()
    SkillLocal.push(skills)

    for i in categories.category:
        if i.title == '개발':
            result = Service.fetch_results(job_group_id=i.id, limit=10000)
            ResultLocal.push(result)
            break


def register_wanted_schedule(scheduler: BackgroundScheduler):
    # scheduled_save_wanted()
    scheduler.add_job(scheduled_save_wanted, 'cron', hour=8, minute=0)
    scheduler.start()
