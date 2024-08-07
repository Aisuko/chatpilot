import fastapi
import uvicorn
import logging


from src.api.endpoints import router as api_endpoint_router


def initialize_app() -> fastapi.FastAPI:
    """
    """

    app=fastapi.FastAPI()

    app.include_router(router=api_endpoint_router, prefix="/api")

    return app

app: fastapi.FastAPI=initialize_app()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port="8000",
        reload="True",
        log_level=logging.INFO
    )
