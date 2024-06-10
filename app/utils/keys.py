import os
from dotenv import load_dotenv
load_dotenv()
SERVICE_KEY = os.environ.get("SERVICE_KEY")
BUS_API_URL = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={SERVICE_KEY}"
BUS_INFO_JSON = r"BNA_BE\app\services\BusInfoData.json"
