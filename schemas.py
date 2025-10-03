from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
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