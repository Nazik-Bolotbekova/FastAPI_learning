from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import Optional

class SighUpModel(BaseModel):
    id: Mapped
    username: Mapped[str] = mapped_column(String(25), unique=True)
    email: Mapped[str] = mapped_column(String(85), unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=True)
    is_staff: Mapped[bool] = mapped_column(default=False)