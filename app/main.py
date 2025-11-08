from fastapi import FastAPI

from app.routers.incidents import router as incidents_router

app = FastAPI(title="Incident Tracker API")
app.include_router(incidents_router)
