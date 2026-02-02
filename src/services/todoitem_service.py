from src.models.todoitem import TodoItem
from src.schemas.todoitem import TodoItemCreate, TodoItemUpdate
from src.repositories.todoitem_repo import TodoItemRepository

class TodoItemService:
    @staticmethod
    async def get_todo_item_by_id(item_id: int) -> TodoItem | None:
        todo_item = await TodoItemRepository.get_by_id(item_id)
        return todo_item

    @staticmethod
    async def create_todo_item(todolist_id: int, item_data: TodoItemCreate) -> TodoItem:
        return await TodoItemRepository.create({
            "todolist_id": todolist_id,
            "description": item_data.description,
            "completed": False
        })

    @staticmethod
    async def update_todo_item(item_id: int, item_data: TodoItemUpdate) -> TodoItem | None:
        todo_item = await TodoItemRepository.get_by_id(item_id)
        if not todo_item:
            return None
        
        update_data = item_data.model_dump(exclude_unset=True)
        return await TodoItemRepository.update(todo_item, update_data)