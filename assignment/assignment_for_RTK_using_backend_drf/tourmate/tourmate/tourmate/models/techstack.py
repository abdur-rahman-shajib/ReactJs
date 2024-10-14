from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from tourmate.models.base import Base

class TechStack(Base):
    __tablename__ = 'techstack'

    name = Column(String(30), nullable=False, primary_key = True)
    code = Column(String(10), nullable=True, default='')
    