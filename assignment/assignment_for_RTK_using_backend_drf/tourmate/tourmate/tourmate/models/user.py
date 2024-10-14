from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from tourmate.models.time_log import TimeLog


class User(TimeLog):
    __tablename__ = 'user'

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    touristplaces = relationship('TouristPlace', back_populates='creator', primaryjoin="User.id == TouristPlace.creator_id")