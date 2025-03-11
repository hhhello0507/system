from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from infra import Local_viewer
from route.AiRoute import ai_router
from route.WantedRoutes import wanted_router

from schedule.WantedSchedule import register_wanted_schedule

app = FastAPI()
scheduler = BackgroundScheduler()

app.include_router(wanted_router)
app.include_router(ai_router)

register_wanted_schedule(scheduler)

Local_viewer.show()