from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from routes.deliver import router as deliver_router

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(title="Genetic OS Delivery Service")

# Include routers
app.include_router(deliver_router, prefix="/deliver", tags=["delivery"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 