from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SessionCreate(BaseModel):
    candidate_id: str


class SessionResponse(BaseModel):
    session_id: UUID
    candidate_id: str
    start_time: datetime
    status: str

    class Config:
        from_attributes = True

from typing import Optional, Dict, Any


class EventCreate(BaseModel):
    session_id: UUID
    event_type: str
    timestamp: int
    payload: Optional[Dict[str, Any]] = None


class EventResponse(BaseModel):
    id: int
    session_id: UUID
    event_type: str
    timestamp: int
    payload: Optional[Dict[str, Any]]

    class Config:
        from_attributes = True