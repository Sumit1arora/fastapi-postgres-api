from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str | None = None

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
