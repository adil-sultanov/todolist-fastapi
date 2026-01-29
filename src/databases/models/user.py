from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    age = fields.IntField(min_value=6, max_value=100, null=True)

    class Meta: # type: ignore[misc]
        table = "users"

    def __str__(self):
        return self.username