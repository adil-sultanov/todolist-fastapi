from pydantic import BaseModel, Field

class TodoListCreate(BaseModel):
    title: str = Field(default="New ToDo List", min_length=1, max_length=255)

class TodoListUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)

class TodoListOut(BaseModel):
    id: int
    title: str