from src.models.todolist import TodoList

class TodoListRepository:
    @staticmethod
    async def create(data: dict) -> TodoList:
        todo_list = await TodoList.create(**data)
        return todo_list

    @staticmethod
    async def get_by_id(list_id: int) -> TodoList | None:
        return await TodoList.get_or_none(id=list_id)

    @staticmethod
    async def update(todo_list: TodoList, data: dict) -> TodoList:
        todo_list.update_from_dict(data)
        await todo_list.save()
        return todo_list