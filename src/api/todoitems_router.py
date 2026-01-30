from fastapi import APIRouter, HTTPException

from src.services.todoitem_service import TodoItemService
from src.schemas.todoitem import TodoItemOut, TodoItemCreate, TodoItemUpdate

router = APIRouter(prefix='/todoitems')

@router.get('/{todoitem_id}', response_model=TodoItemOut)
async def get_todo_item(todoitem_id: int):
    todo_item = await TodoItemService.get_todo_item_by_id(todoitem_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return TodoItemOut.from_orm(todo_item)

@router.post('/{todolist_id}', response_model=TodoItemOut)
async def create_todo_item(todolist_id: int, item_data: TodoItemCreate):
    todo_item = await TodoItemService.create_todo_item(todolist_id, item_data)
    return TodoItemOut.from_orm(todo_item)

@router.put('/{item_id}', response_model=TodoItemOut)
async def update_todo_item(item_id: int, item_data: TodoItemUpdate):
    todo_item = await TodoItemService.update_todo_item(item_id, item_data)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return TodoItemOut.from_orm(todo_item)