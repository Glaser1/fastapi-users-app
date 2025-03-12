import uvicorn

from create_fastapi_app import create_app
from api import router as api_router
from core.config import settings


app = create_app(True)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
