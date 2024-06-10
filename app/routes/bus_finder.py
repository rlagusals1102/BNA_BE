from fastapi import APIRouter, Query
from services.bus_finder_service import bus_finder
from utils.deps import pattern

router = APIRouter()

@router.get("/bus_finder")
async def bus_finder_routes(
        route_id: str = Query(..., regex = pattern),
        stId: str = Query(...,  regex = pattern)
):
    return await bus_finder(route_id, stId)
    
