from fastapi import APIRouter, Query
from services.bus_info_service import get_bus_info
from utils.deps import pattern
router = APIRouter()

@router.get("/bus_info")
async def get_bus_info_route(
        route_id: str = Query(...,  regex=pattern),
        stId: str = Query(..., regex=pattern)
):
    return await get_bus_info(route_id, stId)
