import fastapi

from src.api.routes.health import router as health_router

router=fastapi.APIRouter()

router.include_router(router=health_router)