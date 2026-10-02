from sqlalchemy import Column, Integer, String, Numeric
from app.models.base import Base


class OrderProductDetail(Base):
    __tablename__ = "order_product_details"

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(255))
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255))
    category_name = Column(String(255))
    quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    total_price = Column(Numeric(10, 2))