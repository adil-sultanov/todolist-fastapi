from src.api import get_app
import uvicorn

app = get_app()

uvicorn.run(
    app=app, 
    host="0.0.0.0", 
    port=8000
)