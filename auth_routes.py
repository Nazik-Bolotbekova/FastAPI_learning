from fastapi.exceptions import HTTPException

from fastapi import APIRouter, status
from db import Session, engine
from schemas import SighUpModel
from models import User


router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/authenticate')
async def register():
    return {"message": "Welcome! What is your name?"}

session = Session(bind=engine)

@router.post('/signup')
async def signup(user: SighUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_RQUEST,
            detail='User with that email already exists'
            )

    db_username = session.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with that username already exists'
        )