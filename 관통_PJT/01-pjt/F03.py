from pprint import pprint as print 
import requests

def get_seoul_weather():
    # OpenWeatherMap API 키
    API_KEY = 'fcb6505529a47ac0388b6bce4a17221d'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'


    # API 요청 보내기
    response = requests.get(url).json()
    # print(response)

    key_map = {
        'main': '기본',
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
        'main': '기본상태',
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
        'type' : '타입'
    }

    # data에 전달된 값을 자료형에 따라 다르게 처리
    def translate_keys(data):
        # data == 딕셔너리
        if type(data) == dict:
            new_dict = {}  
            # 원래 딕셔너리의 key들을 하나씩 꺼내면서 반복
            for key in data:  
                # 기존 key를 key_map에서 찾아 한글로 바꿔줌, key_map에 없는 key라면 원래 key 그대로 사용
                new_key = key_map.get(key, key)
                # key에 해당하는 값도 검사 -> 재귀함수 사용
                new_value = translate_keys(data[key]) 
                # 한글 key와 처리된 값을 새로운 딕셔너리에 넣음
                new_dict[new_key] = new_value  
            return new_dict
        # data == 리스트
        elif type(data) == list:
            new_list = []
            # 리스트 안에 있는 요소 하나씩 처리
            for item in data:
                # 리스트 안의 요소도 다시 함수 사용해서 처리 
                new_list.append(translate_keys(item))
            return new_list

        else:
            return data

    response = requests.get(url).json()
    translated = translate_keys(response)
    print(translated)
    return translated

get_seoul_weather()


                

    



        
               