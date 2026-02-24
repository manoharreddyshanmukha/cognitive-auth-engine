from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Event as EventModel
from uuid import UUID

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/features/{session_id}")
def compute_features(session_id: UUID, db: Session = Depends(get_db)):
    events = db.query(EventModel).filter(
        EventModel.session_id == session_id
    ).all()

    # Sort events chronologically
    events.sort(key=lambda x: x.timestamp)

    total_events = len(events)

    # =============================
    # 1️⃣ FIRST KEY DELAY
    # =============================
    question_event = next(
        (e for e in events if e.event_type == "question_shown"),
        None
    )

    first_key_event = next(
        (e for e in events if e.event_type == "keydown"),
        None
    )

    if question_event and first_key_event:
        first_key_delay = first_key_event.timestamp - question_event.timestamp
    else:
        first_key_delay = 0

    # =============================
    # 2️⃣ BASELINE SPLIT
    # =============================
    half_index = len(events) // 2
    baseline_events = events[:half_index]
    current_events = events[half_index:]

    # -----------------------------
    # BASELINE TYPING
    # -----------------------------
    baseline_keydowns = [
        e for e in baseline_events if e.event_type == "keydown"
    ]
    baseline_keydowns.sort(key=lambda x: x.timestamp)

    baseline_flight = []
    for i in range(1, len(baseline_keydowns)):
        delta = baseline_keydowns[i].timestamp - baseline_keydowns[i - 1].timestamp
        baseline_flight.append(delta)

    if baseline_flight:
        baseline_mean = sum(baseline_flight) / len(baseline_flight)
        baseline_variance = sum(
            (x - baseline_mean) ** 2 for x in baseline_flight
        ) / len(baseline_flight)
        baseline_std = baseline_variance ** 0.5
    else:
        baseline_mean = 0
        baseline_std = 1  # prevent division by zero

    # -----------------------------
    # CURRENT TYPING
    # -----------------------------
    current_keydowns = [
        e for e in current_events if e.event_type == "keydown"
    ]
    current_keydowns.sort(key=lambda x: x.timestamp)

    current_flight = []
    for i in range(1, len(current_keydowns)):
        delta = current_keydowns[i].timestamp - current_keydowns[i - 1].timestamp
        current_flight.append(delta)

    if current_flight:
        current_mean = sum(current_flight) / len(current_flight)
    else:
        current_mean = 0

    if baseline_std > 0:
        typing_zscore = (current_mean - baseline_mean) / baseline_std
    else:
        typing_zscore = 0

    # =============================
    # 3️⃣ OVERALL TYPING FEATURES
    # =============================
    keydowns = [e for e in events if e.event_type == "keydown"]
    keydowns.sort(key=lambda x: x.timestamp)

    keydown_count = len(keydowns)

    flight_times = []
    for i in range(1, len(keydowns)):
        delta = keydowns[i].timestamp - keydowns[i - 1].timestamp
        flight_times.append(delta)

    if flight_times:
        mean_flight_time = sum(flight_times) / len(flight_times)

        variance = sum(
            (ft - mean_flight_time) ** 2 for ft in flight_times
        ) / len(flight_times)

        std_flight_time = variance ** 0.5

        pauses = [ft for ft in flight_times if ft > 1000]
        pause_count = len(pauses)
        max_pause = max(pauses) if pauses else 0
    else:
        mean_flight_time = 0
        std_flight_time = 0
        pause_count = 0
        max_pause = 0

    # =============================
    # 4️⃣ TEXT GROWTH MODELING
    # =============================
    text_events = [
        e for e in events if e.event_type == "text_change"
    ]
    text_events.sort(key=lambda x: x.timestamp)

    text_lengths = [
        e.payload.get("text_length", 0)
        for e in text_events
        if e.payload
    ]

    text_deltas = []
    for i in range(1, len(text_lengths)):
        delta = text_lengths[i] - text_lengths[i - 1]
        text_deltas.append(delta)

    if text_deltas:
        max_text_jump = max(text_deltas)
        mean_text_growth = sum(text_deltas) / len(text_deltas)

        growth_variance = sum(
            (d - mean_text_growth) ** 2 for d in text_deltas
        ) / len(text_deltas)

        growth_std_dev = growth_variance ** 0.5
    else:
        max_text_jump = 0
        mean_text_growth = 0
        growth_std_dev = 0

    # =============================
    # 5️⃣ AUTHENTICITY SCORING
    # =============================
    risk_score = 0

    # Typing anomaly risk
    typing_risk = min(abs(typing_zscore) * 2, 25)
    risk_score += typing_risk

    # Large text jump risk
    if max_text_jump > 150:
        growth_risk = 25
    elif max_text_jump > 50:
        growth_risk = 15
    else:
        growth_risk = 0
    risk_score += growth_risk

    # Pause anomaly risk
    if pause_count > 3:
        pause_risk = 15
    else:
        pause_risk = 0
    risk_score += pause_risk

    # First key delay anomaly
    if first_key_delay < 200:
        latency_risk = 15
    else:
        latency_risk = 0
    risk_score += latency_risk

    authenticity_score = max(0, 100 - risk_score)

    if authenticity_score > 80:
        risk_level = "Low"
    elif authenticity_score > 50:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    # =============================
    # RETURN RESPONSE
    # =============================
    return {
        "total_events": total_events,
        "first_key_delay_ms": first_key_delay,
        "keydown_count": keydown_count,
        "mean_flight_time_ms": mean_flight_time,
        "std_flight_time_ms": std_flight_time,
        "pause_count": pause_count,
        "max_pause_ms": max_pause,
        "baseline_mean_flight": baseline_mean,
        "baseline_std_flight": baseline_std,
        "current_mean_flight": current_mean,
        "typing_zscore": typing_zscore,
        "max_text_jump": max_text_jump,
        "mean_text_growth": mean_text_growth,
        "growth_std_dev": growth_std_dev,
        "authenticity_score": authenticity_score,
        "risk_level": risk_level
    }