from pprint import pprint as print 
import requests

# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97

def get_seoul_weather():
    # OpenWeatherMap API 키
    API_KEY = 'bad8adf6c40208aae68eef805c54187e'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

    # API 요청 보내기
    response = requests.get(url).json()
    print(response.keys())
    return response

get_seoul_weather()