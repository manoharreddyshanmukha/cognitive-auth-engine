from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Session as SessionModel
from ..schemas import SessionCreate, SessionResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/session/start", response_model=SessionResponse)
def start_session(session: SessionCreate, db: Session = Depends(get_db)):
    new_session = SessionModel(
        candidate_id=session.candidate_id,
        status="active"
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session