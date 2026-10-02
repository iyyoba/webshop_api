from sqlalchemy import Column, Integer, DateTime, String, text
from app.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    customer_id = Column(
        Integer,
        nullable=False
    )

    order_date = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )

    delivery_date = Column(
        DateTime,
        nullable=True
    )

    shipping_address_id = Column(
        Integer,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=True
    )