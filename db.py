from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql+asyncpg://postgres@localhost:5342/FastAPI', echo=True)

Base = declarative_base()

Session = sessionmaker()