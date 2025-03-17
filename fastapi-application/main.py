import logging
import uvicorn

from create_fastapi_app import create_app
from api import router as api_router
from core.config import settings

logging.basicConfig(format=settings.logging.log_format)
main_app = create_app(True)
main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
