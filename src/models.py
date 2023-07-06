from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class Product(BaseModel):
    id: Optional[UUID] = uuid4
    name: str
    price: int
