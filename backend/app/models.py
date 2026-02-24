import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from .database import Base

class Session(Base):
    __tablename__ = "session"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(String, nullable=False)
    start_time = Column(TIMESTAMP, default=datetime.utcnow)
    end_time = Column(TIMESTAMP, nullable=True)
    status = Column(String, nullable=False)


from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = "event"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.session_id"))
    event_type = Column(String, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    payload = Column(JSONB, nullable=True)