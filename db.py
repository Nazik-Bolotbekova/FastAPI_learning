from fastapi.params import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Annotated
from sqlalchemy.orm import Session

engine = create_engine('postgresql+asyncpg://postgres@localhost:5342/FastAPI', echo=True)

Base = declarative_base()

SessionLocal = sessionmaker()

def  get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]
