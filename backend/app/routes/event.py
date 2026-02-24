from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Event as EventModel
from ..schemas import EventCreate, EventResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/event", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = EventModel(
        session_id=event.session_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        payload=event.payload
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("/events/{session_id}", response_model=list[EventResponse])
def get_events(session_id: str, db: Session = Depends(get_db)):
    events = db.query(EventModel).filter(EventModel.session_id == session_id).all()
    return events