from sqlalchemy import Column, Integer, Numeric
from app.models.base import Base


class OrderItem(Base):
    __tablename__ = "orderitems"

    order_id = Column(
        Integer,
        primary_key=True
    )

    product_id = Column(
        Integer,
        primary_key=True
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    unit_price = Column(
        Numeric(10, 2),
        nullable=False
    )