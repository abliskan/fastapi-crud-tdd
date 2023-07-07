from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import Product

app = FastAPI()

db: List[Product] = [
    Product(
        id=uuid4(),
        name="Gaming Chair",
        price=13400
    )
]


# run: pipenv run uvicorn src.app:app | uvicorn src.app:app
@app.get("/")
async def hello():
    # app_message = os.environ.get("APP_MESSAGE", "Hello")
    return {"message": "Hello World!"}


@app.post('/api/v1/products')
async def create_product(product_data: Product):
    return {
        "name": product_data.name,
        "price": product_data.price
    }


@app.get("/api/v1/products-data")
async def fetch_users():
    return db
