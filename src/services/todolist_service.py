from src.models.todolist import TodoList
from src.schemas.todolist import TodoListCreate, TodoListUpdate
from src.repositories.todolist_repo import TodoListRepository

class TodoListService:
    @staticmethod
    async def get_todo_list_by_id(list_id: int) -> TodoList | None:
        todo_list = await TodoListRepository.get_by_id(list_id)
        return todo_list

    @staticmethod
    async def create_todo_list(user_id: int, list_data: TodoListCreate) -> TodoList:
        return await TodoListRepository.create({
            "user_id": user_id,
            "title": list_data.title
        })

    @staticmethod
    async def update_todo_list(list_id: int, list_data: TodoListUpdate) -> TodoList | None:
        todo_list = await TodoListRepository.get_by_id(list_id)
        if not todo_list:
            return None
        
        update_data = list_data.model_dump(exclude_unset=True)
        return await TodoListRepository.update(todo_list, update_data)