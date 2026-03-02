
from app.services.distance_service import haversine
from app.data.seed_data import customers, warehouses

def calculate_shipping(warehouseId: int, customerId: int, deliverySpeed: str):

    if deliverySpeed.lower() not in ["standard", "express"]:
        return None

    customer = customers.get(customerId)
    warehouse = warehouses.get(warehouseId)

    if not customer or not warehouse:
        return None

    distance = haversine(customer["lat"], customer["lon"], warehouse["lat"], warehouse["lon"])

    weight = 10

    if distance >= 500:
        rate = 1
    elif distance >= 100:
        rate = 2
    else:
        rate = 3

    shipping_cost = distance * rate * weight
    shipping_cost += 10

    if deliverySpeed.lower() == "express":
        shipping_cost += weight * 1.2

    return {"shippingCharge": round(shipping_cost, 2)}
