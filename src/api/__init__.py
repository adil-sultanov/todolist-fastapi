from src.api.users_router import router
from fastapi import FastAPI
from src.databases import database_connect

__all__ = ["router"]

def getapp() -> FastAPI:
    app = FastAPI()
    @app.on_event("startup")
    async def startup():
        await database_connect()
    
    app.include_router(router)
    return app