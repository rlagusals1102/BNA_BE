from fastapi import APIRouter, Query
from services.json_service import get_bus_gps
from utils.deps import pattern
router = APIRouter()

@router.get("/bus_gps")
async def bus_gps_route(
        route_id: str = Query(...,regex=pattern),
        stId: str = Query(...,  regex=pattern)
):
    return await get_bus_gps(route_id, stId)
        