from pprint import pprint as print 
import requests

# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97

def select_data(*keys):
    # OpenWeatherMap API 키
    API_KEY = 'bad8adf6c40208aae68eef805c54187e'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

    dic = {}

    # API 요청 보내기
    response = requests.get(url).json()


    # keys에 있는 각 항목(data)을 하나씩 확인
    for data in keys:
        # 만약 response 딕셔너리에 해당 key(data)가 존재한다면
        if data in response.keys():
            # dic 딕셔너리에 해당 key와 값을 저장
            dic[data] = response[data]
        else:
            # 없으면 아무 작업도 하지 않음
            pass

    # dic 출력 후, None 반환 (print는 반환값이 없음)
    return(print(dic))

    # select_data 함수 실행 
select_data('main', 'weather')



