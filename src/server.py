from src.api import getapp
import uvicorn

app = getapp()

uvicorn.run(
    app=app, 
    host="0.0.0.0", 
    port=8000
)