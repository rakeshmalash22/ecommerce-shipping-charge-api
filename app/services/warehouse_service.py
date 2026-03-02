
from app.services.distance_service import haversine
from app.data.seed_data import customers, warehouses

def get_nearest_warehouse(customerId: int):
    customer = customers.get(customerId)
    if not customer:
        return None

    min_distance = float("inf")
    nearest = None

    for wid, wh in warehouses.items():
        distance = haversine(customer["lat"], customer["lon"], wh["lat"], wh["lon"])
        if distance < min_distance:
            min_distance = distance
            nearest = {"warehouseId": wid, "warehouseLocation": wh}

    return nearest
