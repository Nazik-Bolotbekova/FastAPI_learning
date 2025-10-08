from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Enum
from sqlalchemy_utils import ChoiceType

from enum import OrderStatus, PizzaSize


class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25),unique=True)
    email: Mapped[str] = mapped_column(String(85),unique=True)
    password: Mapped[str] = mapped_column(Text,nullable=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    orders: Mapped['Order'] = relationship(
        'Order',
        back_populates='user'
    )

    def __repr__(self):
        return f"<User {self.username}>"

class Order(Base):

    # ORDER_STATUSES = (
    #     ('PENDING','pending'),
    #     ('IN-TRANSIT','in-transit'),
    #     ('DELIVERED','delivered'),
    # )

    # PIZZA_SIZES = (
    #     ('SMALL','small'),
    #     ('MEDIUM','medium'),
    #     ('LARGE','large'),
    #     ('EXTRA-LARGE','extra large'),
    # )

    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    order_status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus),default=OrderStatus.PENDING ,name='order_status_enum')
    pizza_sizes: Mapped[PizzaSize] = mapped_column(Enum(PizzaSize),default=PizzaSize.SMALL ,name='pizza_size_enum')
    user_id: Mapped[User] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship(
        'User',
        back_populates='orders'
    )

    def __repr__(self):
        return f'<Order: {self.user_id}>'
