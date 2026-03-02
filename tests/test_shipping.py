
from app.services.shipping_service import calculate_shipping

def test_shipping_standard():
    result = calculate_shipping(101, 1, "standard")
    assert result["shippingCharge"] > 0
