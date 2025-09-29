from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy_utils import ChoiceType

from models import Order


class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25),unique=True)
    email: Mapped[str] = mapped_column(String(85),unique=True)
    password: Mapped[str] = mapped_column(Text,nullable=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    order: Mapped['Order'] = relationship(
        'Order',
        back_populates='users'
    )

    def __repr__(self):
        return f"<User {self.username}>"

class Order(Base):

    ORDER_STATUSES = (
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered'),
    )

    PIZZA_SIZES = (
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra large'),
    )

    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    order_status: Mapped[ChoiceType] = mapped_column(choices=ORDER_STATUSES)
    pizza_sizes: Mapped[ChoiceType] = mapped_column(choices=PIZZA_SIZES,default='SMALL')
    user: Mapped[User] = mapped_column(ForeignKey('user.id'))