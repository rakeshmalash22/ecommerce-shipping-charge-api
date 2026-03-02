
from fastapi import FastAPI
from app.routes import warehouse_routes, shipping_routes

app = FastAPI(title="E-Commerce Shipping Charge Estimator")

app.include_router(warehouse_routes.router)
app.include_router(shipping_routes.router)
