from tortoise.models import Model
from tortoise import fields

class TodoItem(Model):
    id = fields.IntField(pk=True)
    todolist = fields.ForeignKeyField("models.TodoList", related_name="items")
    description = fields.CharField(max_length=10000)
    completed = fields.BooleanField(default = False)

    def __str__(self):
        return f"ToDoItem(id={self.id}, todolist_id={self.todolist})"