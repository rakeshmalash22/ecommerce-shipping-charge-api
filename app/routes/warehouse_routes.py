
from fastapi import APIRouter, HTTPException
from app.services.warehouse_service import get_nearest_warehouse

router = APIRouter(prefix="/api/v1/warehouse", tags=["Warehouse"])

@router.get("/nearest")
def nearest_warehouse(customerId: int):
    result = get_nearest_warehouse(customerId)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result
