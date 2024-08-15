import fastapi
import httpx
from src.pkg.utils import httpx_kit

router = fastapi.APIRouter(prefix="/chat", tags=["chat"])


@router.get("", name="chat")
async def chat(
    query: str
) -> dict:

    try:
        response = await httpx_kit.asyn_client.post(
            "http://localhost:8081/embedding",
            headers={"Content-Type": "application/json"},
            json={"content": query},
            timeout=httpx.Timeout(timeout=None),
        )
        response.raise_for_status()
        embedd_input = response.json().get("embedding")
    except httpx.HTTPStatusError as e:
        embedd_input = None


    #TODO: vectordb

    

    return {"Content": embedd_input}


