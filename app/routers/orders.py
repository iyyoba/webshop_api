from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.models.orderitem import OrderItem
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderUpdate
)


router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201
)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db)
):
    order = Order(
        customer_id=order_data.customer_id,
        delivery_date=order_data.delivery_date,
        shipping_address_id=order_data.shipping_address_id,
        status=order_data.status
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order

@router.put(
    "/{order_id}",
    response_model=OrderResponse
)
def update_order(
    order_id: int,
    order_data: OrderUpdate,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.customer_id = order_data.customer_id
    order.delivery_date = order_data.delivery_date
    order.shipping_address_id = order_data.shipping_address_id
    order.status = order_data.status

    db.commit()
    db.refresh(order)

    return order

@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    db.delete(order)
    db.commit()

    return {
        "message": "Order deleted successfully"
    }


###
@router.post("/with-item")
def create_order_with_item(
    order_data: OrderCreate,
    product_id: int,
    quantity: int,
    unit_price: float,
    db: Session = Depends(get_db)
):
    try:
        # Create the order
        order = Order(
            customer_id=order_data.customer_id,
            delivery_date=order_data.delivery_date,
            shipping_address_id=order_data.shipping_address_id,
            status=order_data.status
        )

        db.add(order)
        db.flush()

        # Create the order item
        order_item = OrderItem(
            order_id=order.id,
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price
        )

        db.add(order_item)

        # Save both operations
        db.commit()

        db.refresh(order)

        return {
            "message": "Order and order item created successfully",
            "order_id": order.id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price
        }

    except Exception as error:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=f"Transaction failed: {error}"
        )