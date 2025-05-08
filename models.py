from sqlalchemy import Column, String, UUID, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

Base = declarative_base()

class GeneticReport(Base):
    __tablename__ = "genetic_reports"
    
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID)
    raw_assistant_response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    user = relationship("User", back_populates="reports")

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True)
    email = Column(String)
    reports = relationship("GeneticReport", back_populates="user") 