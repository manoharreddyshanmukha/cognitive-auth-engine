from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import Base
from .routes import session
from .routes import event
from .routes import feature

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(session.router)
app.include_router(event.router)
app.include_router(feature.router)


@app.get("/")
def root():
    return {"message": "Backend is running"}