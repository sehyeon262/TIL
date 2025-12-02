import requests
from pprint import pprint as print  # 보기 좋게 출력

def get_seoul_weather():
    # 1. API 요청
    API_KEY = 'fcb6505529a47ac0388b6bce4a17221d'
    lat = 37.56
    lon = 126.97
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url).json()

    # 2. 키 번역 맵
    key_map = {
        'main': '기본상태',
        'temp': '온도',
        'feels_like': '체감온도',
        'temp_min': '최저기온',
        'temp_max': '최고기온',
        'pressure': '기압',
        'humidity': '습도',
        'sea_level': '해수면기압',
        'grnd_level': '지면기압',
        'weather': '날씨',
        'description': '설명',
        'icon': '아이콘',
        'id': '상태ID',
        'clouds': '구름',
        'all': '전체',
        'wind': '바람',
        'speed': '풍속',
        'deg': '풍향',
        'dt': '데이터시간',
        'sys': '시스템',
        'country': '국가',
        'sunrise': '일출',
        'sunset': '일몰',
        'timezone': '시간대',
        'coord': '좌표',
        'lat': '위도',
        'lon': '경도',
        'visibility': '가시거리',
        'name': '도시이름',
        'base': '관측기반',
        'cod': '응답코드',
        'type': '타입'
    }

    # 3. 키 번역 + 섭씨 추가 함수
    def translate_keys(data):
        # 데이터가 딕셔너리일 때 
        if isinstance(data, dict):
            new_dict = {}

            # 원래 딕셔너리의 key와 value를 하나씩 반복
            for key in data:
                value = data[key]
                # key_map에서 영어 key를 찾아 한글로 바꾸기 (없으면 그대로 사용)
                new_key = key_map.get(key, key)
                # value도 다시 확인해서 처리 (딕셔너리나 리스트일 수 있으니까 재귀 호출)
                new_value = translate_keys(value)
                # 새로운 한글 key와 번역된 value를 새 딕셔너리에 저장
                new_dict[new_key] = new_value

                # 섭씨 온도 추가 조건 (숫자일 때만 추가)
                if key in ['temp', 'feels_like', 'temp_min', 'temp_max']:
                    if isinstance(value, (int, float)):
                        # "온도" → "온도(섭씨)"처럼 key 이름 뒤에 (섭씨)를 붙임
                        celsius_key = new_key + '(섭씨)'
                        # 섭씨 = 켈빈 - 273.15, 소수점 둘째 자리까지 반올림
                        new_dict[celsius_key] = round(value - 273.15, 2)
            return new_dict

        # 데이터가 리스트일 때 
        elif isinstance(data, list):
            # 리스트 안의 모든 항목에 translate_keys 함수를 다시 적용
            return [translate_keys(item) for item in data]

        # 그 외의 경우(숫자, 문자열 )
        else:
            return data

    # 변환 실행 및 출력
    translated = translate_keys(response)
    print(translated)
    return translated

get_seoul_weather()

