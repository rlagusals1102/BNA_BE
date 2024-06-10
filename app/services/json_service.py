from json import load, JSONDecodeError
from utils.keys import BUS_INFO_JSON

# NOTE : 노선, 정류장 ID에 해당하는 GPS 좌표 반환
async def get_bus_gps(route_id: str, stId: str):

    with open(BUS_INFO_JSON, 'r', encoding='utf-8') as file:
        data = load(file)

    for item in data:
        if item.get('ROUTE_ID') == route_id and item.get('NODE_ID') == stId:
            return {'x_point': item.get('X좌표'), 'y_point': item.get('Y좌표')}
