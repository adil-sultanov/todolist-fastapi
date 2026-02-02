from tortoise import Tortoise
from src.config.settings import settings

database_config = {
    "connections": {
        "default": settings.DATABASE_URL
    },
    "apps": {
        "models": {
            "models": ["src.models"],
            "default_connection": "default",
        }
    }
}

async def database_connect():
    await Tortoise.init(
        config = database_config
    )