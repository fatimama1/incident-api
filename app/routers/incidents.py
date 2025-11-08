from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import create_incident, get_incidents, update_status
from app.database import get_db
from app.schemas import IncidentCreate, IncidentOut, IncidentStatus

router = APIRouter(prefix="/incidents", tags=["incidents"])

get_db_dependency = Depends(get_db)


@router.post("/", response_model=IncidentOut)
async def create_incident_endpoint(
    incident: IncidentCreate, db: AsyncSession = get_db_dependency
):
    new_incident = await create_incident(db, incident)
    return new_incident


@router.get("/", response_model=list[IncidentOut])
async def list_incidents(
    status: IncidentStatus | None = None, db: AsyncSession = get_db_dependency
):
    incidents = await get_incidents(db, status)
    return incidents


@router.patch("/{incident_id}/status", response_model=IncidentOut)
async def change_status(
    incident_id: int, status: IncidentStatus, db: AsyncSession = get_db_dependency
):
    incident = await update_status(db, incident_id, status)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident
