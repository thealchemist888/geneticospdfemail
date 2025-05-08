from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    logger.error("DATABASE_URL environment variable is not set")
    raise ValueError("DATABASE_URL environment variable is not set")

try:
    # Configure SQLAlchemy for PostgreSQL with SSL mode require
    if "postgresql" in DATABASE_URL:
        if "?" in DATABASE_URL:
            DATABASE_URL += "&sslmode=require"
        else:
            DATABASE_URL += "?sslmode=require"
    
    logger.info("Connecting to database...")
    engine = create_engine(
        DATABASE_URL,
        poolclass=NullPool,  # Disable connection pooling
        connect_args={
            "connect_timeout": 10  # Set connection timeout to 10 seconds
        }
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database connection established successfully")
except Exception as e:
    logger.error(f"Failed to connect to database: {str(e)}")
    raise 