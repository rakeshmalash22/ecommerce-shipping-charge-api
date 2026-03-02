
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.warehouse_service import get_nearest_warehouse
from app.services.shipping_service import calculate_shipping

router = APIRouter(prefix="/api/v1/shipping-charge", tags=["Shipping"])

@router.get("")
def shipping_charge(warehouseId: int, customerId: int, deliverySpeed: str):
    result = calculate_shipping(warehouseId, customerId, deliverySpeed)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid input")
    return result


class ShippingRequest(BaseModel):
    sellerId: int
    customerId: int
    deliverySpeed: str


@router.post("/calculate")
def calculate_combined_shipping(data: ShippingRequest):

    nearest = get_nearest_warehouse(data.customerId)
    if not nearest:
        raise HTTPException(status_code=404, detail="Customer not found")

    result = calculate_shipping(
        nearest["warehouseId"],
        data.customerId,
        data.deliverySpeed
    )

    if not result:
        raise HTTPException(status_code=400, detail="Invalid input")

    return {
        "shippingCharge": result["shippingCharge"],
        "nearestWarehouse": nearest
    }
