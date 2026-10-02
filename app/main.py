from fastapi import FastAPI

from app.routers.customers import router as customers_router
from app.routers.products import router as products_router
from app.routers.orders import router as orders_router
from app.routers.orderitems import router as orderitems_router
from app.routers.order_product_details import (
    router as order_product_details_router
)

app = FastAPI(
    title="Webshop Order Management API",
    version="1.0.0"
)

app.include_router(customers_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(orderitems_router)
app.include_router(order_product_details_router)


@app.get("/")
def root():
    return {
        "message": "Webshop API is running"
    }