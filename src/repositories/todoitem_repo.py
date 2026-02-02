from src.models.todoitem import TodoItem

class TodoItemRepository:
    @staticmethod
    async def create(data: dict) -> TodoItem:
        todo_item = await TodoItem.create(**data)
        return todo_item

    @staticmethod
    async def get_by_id(item_id: int) -> TodoItem | None:
        return await TodoItem.get_or_none(id=item_id)

    @staticmethod
    async def update(todo_item: TodoItem, data: dict) -> TodoItem:
        todo_item.update_from_dict(data)
        await todo_item.save()
        return todo_item