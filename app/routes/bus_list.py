from fastapi import APIRouter, Query
from services.bus_list_service import bus_list
from utils.deps import pattern
router = APIRouter()

@router.get("/bus_list")
async def bus_list_routes(
        route_id: str = Query(...,  regex=pattern),
        stId: str = Query(...,  regex=pattern)
):
    return await bus_list(route_id, stId)