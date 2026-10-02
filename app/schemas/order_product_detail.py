from decimal import Decimal
from pydantic import BaseModel


class OrderProductDetailResponse(BaseModel):
    customer_id: int
    customer_name: str
    order_id: int
    product_id: int
    product_name: str
    category_name: str
    quantity: int
    unit_price: Decimal
    total_price: Decimal

    class Config:
        from_attributes = True