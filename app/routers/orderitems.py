from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.orderitem import OrderItem
from app.schemas.orderitem import (
    OrderItemCreate,
    OrderItemResponse,
    OrderItemUpdate
)


router = APIRouter(
    prefix="/api/orderitems",
    tags=["Order Items"]
)


@router.get(
    "/",
    response_model=list[OrderItemResponse]
)
def get_order_items(
    db: Session = Depends(get_db)
):
    order_items = db.query(OrderItem).all()
    return order_items


@router.get(
    "/{order_id}/{product_id}",
    response_model=OrderItemResponse
)
def get_order_item(
    order_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):
    order_item = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == order_id,
            OrderItem.product_id == product_id
        )
        .first()
    )

    if order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    return order_item


@router.post(
    "/",
    response_model=OrderItemResponse,
    status_code=201
)
def create_order_item(
    item_data: OrderItemCreate,
    db: Session = Depends(get_db)
):
    existing_item = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == item_data.order_id,
            OrderItem.product_id == item_data.product_id
        )
        .first()
    )

    if existing_item is not None:
        raise HTTPException(
            status_code=400,
            detail="This product already exists in the order"
        )

    order_item = OrderItem(
        order_id=item_data.order_id,
        product_id=item_data.product_id,
        quantity=item_data.quantity,
        unit_price=item_data.unit_price
    )

    db.add(order_item)
    db.commit()
    db.refresh(order_item)

    return order_item
@router.put(
    "/{order_id}/{product_id}",
    response_model=OrderItemResponse
)
def update_order_item(
    order_id: int,
    product_id: int,
    item_data: OrderItemUpdate,
    db: Session = Depends(get_db)
):
    order_item = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == order_id,
            OrderItem.product_id == product_id
        )
        .first()
    )

    if order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    order_item.quantity = item_data.quantity
    order_item.unit_price = item_data.unit_price

    db.commit()
    db.refresh(order_item)

    return order_item


@router.delete(
    "/{order_id}/{product_id}"
)
def delete_order_item(
    order_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):
    order_item = (
        db.query(OrderItem)
        .filter(
            OrderItem.order_id == order_id,
            OrderItem.product_id == product_id
        )
        .first()
    )

    if order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    db.delete(order_item)
    db.commit()

    return {
        "message": "Order item deleted successfully"
    }