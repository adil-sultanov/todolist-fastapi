from users_router import router
from fastapi import FastAPI

__all__ = ["router"]

def getapp() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app