import fastapi


router = fastapi.APIRouter(prefix="/health", tags=["health"])


@router.get("", name="health:health-check")
async def health_check() -> dict:
    return {"Status": "Ok"}