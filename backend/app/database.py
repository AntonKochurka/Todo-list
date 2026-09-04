from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(
    url="",
    echo=True
)

Session = sessionmaker(engine, autoflush=False)

def get_session():
    session = Session()

    try:
        yield session
    finally:
        session.close()