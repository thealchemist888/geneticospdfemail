from sqlalchemy import Column, String, UUID, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GeneticReport(Base):
    __tablename__ = "genetic_reports"
    
    report_id = Column(UUID, primary_key=True)
    user_id = Column(UUID)
    raw_assistant_response = Column(Text)

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(UUID, primary_key=True)
    email = Column(String) 