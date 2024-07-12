# -*- coding: utf-8 -*-
import serial
import pynmea2

# 시리얼 포트 설정
port = '/dev/ttyTHS1'  # 연결된 GPS 모듈의 시리얼 포트명에 따라 수정

# 현재위치 정보 텍스트 형식으로 저장
def save_gps_data(latitude, longitude):
    with open("gps_data.txt", "a") as file:
        file.write("Latitude: {}, Longitude: {}\n".format(latitude, longitude))


def read_gps_data(ser):
    while True:
        try:
            print("1")
            line = ser.readline().decode('utf-8')  # GPS 데이터 읽기
            print("2")
            print(line)  # line 변수 출력
            print("3")  # 3 출력
            msg = pynmea2.parse(line)  # NMEA 데이터 파싱
            print(msg)  # 파싱된 데이터 출력
            print("4")  # 4 출력
            #print("현재 위치: 위도 {}, 경도 {}".format(msg.latitude, msg.longitude)) # 위치값 출력
            if line[0:6] == ('$GPGGA'):  # 메시지인지 확인
                print("5")  
                msg = pynmea2.parse(line)  # NMEA 데이터 파싱
                print(msg)  # 파싱된 데이터 출력
                print("현재 위치: 위도 {}, 경도 {}".format(msg.latitude, msg.longitude)) # 위치값 출력
                save_gps_data(msg.latitude, msg.longitude)  # GPS 데이터 저장

        except serial.SerialException:
            print("시리얼 통신 오류 발생!")
            break
        except pynmea2.nmea.ParseError as e:
            print("NMEA 데이터 파싱 오류:", e)

def main():
    try:
        # 시리얼 포트 열기
        ser = serial.Serial(port, baudrate=115200, timeout=1)
        print("시리얼 포트 연결 성공!")
        
        # GPS 데이터 읽기
        read_gps_data(ser)
    except serial.SerialException:
        print("시리얼 포트 연결 실패!")

if __name__ == "__main__":
    main()