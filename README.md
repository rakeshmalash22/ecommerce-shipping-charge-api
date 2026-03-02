# 🚀 E-Commerce Shipping Charge Estimator (FastAPI)

A FastAPI-based backend system that calculates shipping charges based on:

- Nearest warehouse resolution
- Distance-based pricing logic
- Delivery speed (Standard / Express)

This project demonstrates REST API design, modular architecture, and backend business logic implementation.

---

## 📷 API Documentation Preview

![https://drive.google.com/file/d/1N2uZhNC5iyWXpV_jUEU4JKlQ8Z3fj6L-/view?usp=drive_link](picture.jpg)

---

## 🧠 Features

- Find nearest warehouse using customer location
- Calculate shipping cost based on distance
- Delivery speed pricing multiplier
- Clean modular project structure
- Auto-generated Swagger API docs
- Input validation using Pydantic

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- REST API Architecture

---

## 📂 Project Structure

app/
 ├── main.py  
 ├── routers/  
 ├── services/  
 ├── models/  

tests/  
requirements.txt  
README.md  

---

## 📌 API Endpoints

### 1️⃣ Get Nearest Warehouse
GET /api/v1/warehouse/nearest?customerId=1

### 2️⃣ Calculate Shipping (Query Params)
GET /api/v1/shipping-charge?warehouseId=102&customerId=1&deliverySpeed=standard

### 3️⃣ Calculate Combined Shipping
POST /api/v1/shipping-charge/calculate

### Sample Request Body

```json
{
  "sellerId": 123,
  "customerId": 1,
  "deliverySpeed": "express"
}
```

---

## ▶️ How To Run Locally

### Step 1: Create virtual environment
python -m venv venv

### Step 2: Activate (Windows)
venv\Scripts\activate

### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Run server
uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

---

## 🧮 Business Logic

Shipping charge is calculated based on:

- Distance between customer and nearest warehouse
- Base rate per kilometer
- Delivery speed multiplier

---

## 🎯 Why This Project?

This project demonstrates:

- Backend API development
- Clean architecture design
- Distance-based calculation logic
- Real-world e-commerce use case

---

## 👨‍💻 Author

Rakesh Malash  
B.Tech CSE (2026 Passout)  
College of Engineering and Management, Kolaghat
