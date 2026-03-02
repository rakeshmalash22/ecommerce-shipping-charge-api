
# E-Commerce Shipping Charge Estimator (Final Version)

APIs:
1. GET /api/v1/warehouse/nearest
2. GET /api/v1/shipping-charge
3. POST /api/v1/shipping-charge/calculate

Run:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
