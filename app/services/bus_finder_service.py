"""
NOTE : 노선, 정류장 ID에 대응하는 버스 정보 조회 
현재 정류장을 기준으로 이전, 다음 버스 정보 반환
"""

import httpx
import xml.etree.ElementTree as ET

from utils.keys import BUS_API_URL
from utils.deps import extract_bus_info


async def bus_finder(route_id: str, stId: str):
    url = f"{BUS_API_URL}&busRouteId={route_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    response_content = response.text

    root = ET.fromstring(response_content)
    items = root.findall(".//itemList")

    for i, item in enumerate(items):
        if item.find('stId').text == stId:
            prev_info = await extract_bus_info(items[i - 1]) if i > 0 else None
            next_info = await extract_bus_info(items[i + 1]) if i < len(items) - 1 else None

            return {
                "prev_info": prev_info,
                "next_info": next_info
            }