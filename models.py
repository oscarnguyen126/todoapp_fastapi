from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=True)


Base.metadata.create_all(engine)
