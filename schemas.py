from pydantic import BaseModel
from typing import Optional

class SighUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class Config:
        orm_mode = True
        scheme_extra = {
            'example' : {
                'username': 'thenaziazi',
                'email': 'bolotbekova09@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True,
            }
        }


class Settings(BaseModel):
    jwt_secret_key: str='f8021a2400469bd30d1d907a0aebb8a740986ea75e289a6cb0dd2c728a8b863a'


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

