from decimal import Decimal

from pydantic import BaseModel


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    unit_price: Decimal


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    quantity: int
    unit_price: Decimal


class OrderItemResponse(OrderItemBase):

    class Config:
        from_attributes = True