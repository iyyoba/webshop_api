from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order_product_detail import OrderProductDetail
from app.schemas.order_product_detail import OrderProductDetailResponse


router = APIRouter(
    prefix="/api/order-details",
    tags=["Order Details"]
)


@router.get(
    "/",
    response_model=list[OrderProductDetailResponse]
)
def get_order_details(
    db: Session = Depends(get_db)
):
    details = db.query(OrderProductDetail).all()

    return details