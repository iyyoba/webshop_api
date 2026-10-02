from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_id: int
    order_date: datetime
    delivery_date: datetime | None = None
    shipping_address_id: int | None = None
    status: str | None = "NEW"


class OrderCreate(BaseModel):
    customer_id: int
    delivery_date: datetime | None = None
    shipping_address_id: int | None = None
    status: str | None = "NEW"


class OrderUpdate(BaseModel):
    customer_id: int
    delivery_date: datetime | None = None
    shipping_address_id: int | None = None
    status: str | None = None


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True