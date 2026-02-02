from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    age = fields.IntField(min_value=1, max_value=100, null=True)
    hashed_password = fields.CharField(max_length=256, null=True)

    class Meta: # type: ignore[misc]
        table = "users"

    def __str__(self):
        return self.username