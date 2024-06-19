# Bus NFC Application [Server]
`2023 Web/APP Project`<br>
기간 : 2023.11.28 ~ 2023.12.08<br>

## 개요
NFC Tag를 활용한 실시간 버스 위치 확인 앱입니다. 용산 03 마을버스 정류장 중 절반은 표지판을 통해 실시간 버스 정보를 받을 수 없는 문제점을 가지고 있습니다. 이를 해결하기 위해 NFC 스티커를 사용하여 쉽게 정보를 제공할 수 있도록 하였습니다.

## 주요 기능
- 실시간 버스 위치 확인: NFC 스티커를 통해 사용자가 버스 정류장에서 실시간으로 버스 도착 정보를 확인할 수 있습니다.
- 버스 노선 정보 조회: 사용자가 선택한 버스의 노선 정보를 조회할 수 있습니다.

## API 사용처
- Kakao Map API
- [공공데이터포털 - 버스도착정보조회](https://www.data.go.kr/data/15000314/openapi.do)
   - 실시간 버스 도착 정보를 조회하기 위해 사용된 공공 데이터 포털의 API입니다.
-  [공공데이터포털 - 노선정보조회](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000193)
   - 버스 노선 정보 조회  API입니다.
- [API 전처리 및 통신](https://github.com/rlagusals1102/Bus-NFC-Application/tree/main/BNA_server)
  - FastAPI

## 설정
1. **라이브러리 설치**
   ```bash
   pip install -r requirements.txt
   ```
2. **서버 실행**
   ```bash
   uvicorn app.main:app --reload
   ```

## API 명세서
   | 엔드포인트     | 메소드 | 파라미터                                   | 설명                                               |
   |----------------|--------|--------------------------------------------|----------------------------------------------------|
   | `/bus_finder`  | GET    | route_id (str), stId (str)                 | 현재 정류장을 중심으로 이전, 다음 버스 조회 |
   | `/bus_gps`     | GET    | route_id (str), stId (str)                 | 버스의 정류장 GPS                       |
   | `/bus_info`    | GET    | route_id (str), stId (str)                 | 현재 정류장 버스 조회                      |
   | `/bus_list`    | GET    | route_id (str), stId (str)                 | 현재 위치에 있는 버스 정류장 이름으로 정류장의 모든 버스 제공 |
