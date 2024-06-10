"""
NOTE : 현재 위치에 있는 버스 정류장 이름으로 정류장의 모든 버스 list 반환
"""

import httpx
import json
import xml.etree.ElementTree as ET
from utils.keys import BUS_API_URL,BUS_INFO_JSON


async def bus_list(route_id: str, stId: str):
    url = f"{BUS_API_URL}&busRouteId={route_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    response_content = response.text

    root = ET.fromstring(response_content)
    stNm = None

    for itemList in root.findall('.//itemList'):
        if itemList.find('stId').text == stId:
            stNm = itemList.find('stNm').text
    
    return await route_information(stNm, stId)


async def route_information(name: str, stId: str):
    ans = []

    with open(BUS_INFO_JSON, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for item in data:
            if item.get('정류소명') == name and item.get('NODE_ID') == stId:
                ans.append(item.get('노선명'))

        return list(ans)
