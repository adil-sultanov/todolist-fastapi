from src.auth import router as auth_router
from src.api.users_router import router as users_router
from src.api.todoitems_router import router as todoitems_router
from src.api.todolists_router import router as todolists_router
from fastapi import FastAPI
from src.databases import database_connect

__all__ = ["users_router"]
def get_app() -> FastAPI:
    app = FastAPI()
    @app.on_event("startup")
    async def startup():
        await database_connect()
    
    app.include_router(users_router)
    app.include_router(todolists_router)
    app.include_router(todoitems_router)
    app.include_router(auth_router)

    return app