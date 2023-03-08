from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="admin123",
    host="localhost",
    database="todo_db",
    port=5433
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
