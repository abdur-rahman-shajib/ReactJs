from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from tourmate.models.time_log import TimeLog


class TouristPlace(TimeLog):
    __tablename__ = 'touristplace'

    name = Column(String(30), nullable=False, default='')
    address = Column(String(100), nullable=True, default='')
    place_type = Column(String(20), nullable=False, default='hill')
    rating = Column(Integer, default=4, index=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    picture = Column(Text, default='', nullable=True)
    
    creator = relationship('User', back_populates='touristplaces', primaryjoin="TouristPlace.creator_id == User.id")