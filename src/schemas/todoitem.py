from pydantic import BaseModel, Field

class TodoItemCreate(BaseModel):
    description: str = Field(min_length=1, max_length=10000)

class TodoItemUpdate(BaseModel):
    description: str | None = None
    completed: bool | None = None

class TodoItemOut(BaseModel):
    id: int
    description: str
    completed: bool

class TodoItemListOut(BaseModel):
    items: list[TodoItemOut]
    total: int