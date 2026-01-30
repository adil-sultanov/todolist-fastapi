from fastapi import APIRouter, HTTPException
from src.services.todolist_service import TodoListService
from src.schemas.todolist import TodoListOut, TodoListCreate, TodoListUpdate

router = APIRouter(prefix='/todolists')
@router.get('/{todolist_id}', response_model=TodoListOut)
async def get_todo_list(todolist_id: int):
    todolist = await TodoListService.get_todo_list_by_id(todolist_id)
    if not todolist:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return TodoListOut.from_orm(todolist)