from tortoise.models import Model
from tortoise import fields

class ToDoItem(Model):
    id = fields.IntField(pk=True)
    todolist = fields.ForeignKeyField("models.ToDoList", related_name="items")
    desc = fields.CharField(max_length=10000)

    def __str__(self):
        return f"ToDoItem(id={self.id}, todolist_id={self.todolist})"