from tortoise.models import Model
from tortoise import fields

class ToDoList(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="todolists")
    description = fields.TextField()

    class Meta: # type: ignore[misc]
        table = "To do lists"
    
    def __str__(self):
        return f"ToDoList(id={self.id}, userID={self.user}, description={self.description})"