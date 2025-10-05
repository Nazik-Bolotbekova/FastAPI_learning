from fastapi import APIRouter
from db import Session, engine
from schemas import SighUpModel

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/authenticate')
async def register():
    return {"message": "Welcome! What is your name?"}

session = Session(bind=engine)

@router.post('/signup')
async def signup()