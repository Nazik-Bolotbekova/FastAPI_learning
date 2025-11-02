from fastapi.exceptions import HTTPException

from fastapi import APIRouter, status
from db import Session, engine
from schemas import SighUpModel
from models import User

import logging

from werkzeug.security import generate_password_hash, check_password_hash


router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/authenticate')
async def register():
    return {"message": "Welcome! What is your name?"}

session = Session(bind=engine)

@router.post('/signup',
             status_code=status.HTTP_201_CREATED)
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

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active,
    )

    session.add(new_user)

    session.commit()

    return new_user


