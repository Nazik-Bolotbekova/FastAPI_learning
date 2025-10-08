from enum import Enum



class OrderStatus(str, Enum):
    PENDING = 'pending'
    IN_TRANSIT = 'in-transit'
    DELIVERED = 'delivered'


class PizzaSize(str, Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra large'