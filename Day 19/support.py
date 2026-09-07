from enum import StrEnum
from dataclasses import dataclass

class OrderStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        else:
            return None

@dataclass
class Order:
    order_id: int
    status: OrderStatus = OrderStatus.PENDING

    def startProcessing(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.PROCESSING
        else:
            raise ValueError(f"Cannot start processing an order that is {self.status.value}.")

    def ship(self):
        if self.status == OrderStatus.PROCESSING:
            self.status = OrderStatus.SHIPPED
        else:
            raise ValueError(f"Cannot ship an order that is {self.status.value}.")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
        else:
            raise ValueError(f"Cannot deliver an order that is {self.status.value}.")

    def cancel(self):
        if self.status in [OrderStatus.PENDING, OrderStatus.PROCESSING]:
            self.status = OrderStatus.CANCELLED
        else:
            raise ValueError(f"Cannot cancel an order that is {self.status.value}.")