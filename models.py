from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from sqlalchemy_utils import ChoiceType

class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25),unique=True)
    email: Mapped[str] = mapped_column(String(85),unique=True)
    password: Mapped[str] = mapped_column(Text,nullable=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)


    def __repr__(self):
        return f"<User {self.username}>"

class Choice(Base):

    ORDER_STATUSES = (
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered'),
    )

    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    order_status: Mapped[ChoiceType] = mapped_column(choices=ORDER_STATUSES)
