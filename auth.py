from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from starlette import status
from db import db_dependency

from models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt

from schemas import SighUpModel

router = APIRouter(
    prefix='/auth',
    tags=['/auth']
)

SECRET_KEY = "a22645d04029129ae736fe1859a8fe0cc04a5910e8555ac10f0d2ca76dcd5662"
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # создаем контекста с несколькими алгоритмами
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, sighup_model: SighUpModel):
    create_user_model = User(username=sighup_model.username,
                             password=bcrypt_context.hash(sighup_model.password))

    db.add(create_user_model)
    db.commit()