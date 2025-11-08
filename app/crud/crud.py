from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Incident, IncidentStatus
from app.schemas import IncidentCreate


async def create_incident(db: AsyncSession, incident: IncidentCreate):
    new_incident = Incident(description=incident.description, source=incident.source)
    db.add(new_incident)
    await db.commit()
    await db.refresh(new_incident)
    return new_incident


async def get_incidents(db: AsyncSession, status: IncidentStatus | None = None):
    stmt = select(Incident)
    if status:
        stmt = stmt.filter(Incident.status == status)
    result = await db.execute(stmt)
    return result.scalars().all()


async def update_status(db: AsyncSession, incident_id: int, status: IncidentStatus):
    stmt = select(Incident).filter(Incident.id == incident_id)
    result = await db.execute(stmt)
    incident = result.scalar_one_or_none()
    if not incident:
        return None
    incident.status = status
    await db.commit()
    await db.refresh(incident)
    return incident
