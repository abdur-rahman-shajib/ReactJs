from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from tourmate.models.base import Base

class EnosisProject(Base):
    __tablename__ = 'enosis_project'

    name = Column(String(30), nullable=False, primary_key = True)
    mode = Column(String(10), nullable=True, default='')
    client = Column(String(30), nullable=True, default='')

    se_count = Column(Integer, nullable=True, default=13)
    sse_count = Column(Integer, nullable=True, default=3)
    total_resources = Column(Integer, nullable=True, default=6)
    non_lead_resources = Column(Integer, nullable=True, default=4)
    planned = Column(Boolean, nullable=True, default=True)
    
    manager = Column(String(30), nullable=True, default='manager')
    lead = Column(String(30), nullable=True, default='lead')
    dev_lead = Column(String(30), nullable=True, default='dev_lead')
    tech_lead = Column(String(30), nullable=True, default='tech leads')
    buffer = Column(Integer, nullable=True, default=1)

    archived = Column(Integer, nullable=True, default=False)
    