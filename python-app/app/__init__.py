from fastapi import FastAPI

from .api.routes import router
from .config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.app_description,
    )

    app.include_router(router, prefix="/api")

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    return app
