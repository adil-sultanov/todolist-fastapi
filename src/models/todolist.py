from tortoise.models import Model
from tortoise import fields

class TodoList(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="todolists")
    title = fields.TextField()

    class Meta: # type: ignore[misc]
        table = "To do lists"
    
    def __str__(self):
        return f"TodoList(id={self.id}, userID={self.user}, description={self.title})"