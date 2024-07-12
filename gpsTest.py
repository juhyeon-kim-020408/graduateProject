import folium

# Folium 지도 초기화
map_folium = folium.Map(location=[37.3783, 127.1144], zoom_start=13)  # 초기 맵 중심을 수내역으로 설정

# 이동 경로를 저장할 리스트
route_points = []

# 마커를 표시하는 함수
def add_marker(location):
    folium.Marker(location=location, popup=f'{location}').add_to(map_folium)
    map_folium.save('realtime_gps_route.html')

# 이동 경로를 그리는 함수
def draw_route(start, end):
    global route_points
    route_points = [start, end]
    folium.PolyLine(locations=route_points, color='blue').add_to(map_folium)
    map_folium.save('realtime_gps_route.html')

# 첫 번째 위치의 위도 입력
start_latitude = float(input("첫 번째 위치의 위도를 입력하세요 : "))

# 첫 번째 위치의 경도 입력
start_longitude = float(input("첫 번째 위치의 경도를 입력하세요 : "))

# 첫 번째 위치의 좌표
start_location = (start_latitude, start_longitude)
add_marker(start_location)

# 위치 입력 루프
try:
    while True:
        # 새로운 위치의 위도 입력
        new_latitude = float(input("새로운 위치의 위도를 입력하세요 : "))
        
        # 새로운 위치의 경도 입력
        new_longitude = float(input("새로운 위치의 경도를 입력하세요 : "))

        # 새로운 위치의 좌표
        new_location = (new_latitude, new_longitude)
        draw_route(start_location, new_location)
        add_marker(new_location)
        start_location = new_location
except KeyboardInterrupt:
    pass

# 맵을 초기화하고 HTML 파일로 저장
map_folium = folium.Map(location=[37.3783, 127.1144], zoom_start=13)  # 초기 맵 중심을 수내역으로 설정
map_folium.save('realtime_gps_route.html')