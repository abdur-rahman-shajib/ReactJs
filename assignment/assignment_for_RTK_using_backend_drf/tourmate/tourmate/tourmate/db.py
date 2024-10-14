from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

from tourmate.models.base import Base


DATABASE_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DATABASE_URL)

LocalSession = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(bind=engine)