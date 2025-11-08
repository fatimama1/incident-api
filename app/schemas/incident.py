from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class IncidentStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class IncidentBase(BaseModel):
    description: str
    source: str


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    status: IncidentStatus


class IncidentOut(IncidentBase):
    id: int
    status: IncidentStatus
    created_at: datetime

    class Config:
        from_attributes = True
