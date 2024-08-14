import fastapi

from src.api.routes.health import router as health_router
from src.api.routes.chat import router as chat_router

router=fastapi.APIRouter()

router.include_router(router=health_router)
router.include_router(router=chat_router)