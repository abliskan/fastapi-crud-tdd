from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime


class Product(BaseModel):
    id: Optional[UUID] = uuid4
    name: str
    price: int
    created_by: Optional[str] = None
    created_at: datetime = datetime.now()
