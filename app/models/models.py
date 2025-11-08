import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String, func

from app.database import Base


class IncidentStatus(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.open)
    source = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
