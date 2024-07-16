import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import paramiko

# Import CameraViewer class from noirCameraTest.py
from noirCameraTest import CameraViewer

# 라즈베리 파이의 SSH 접속 정보
raspberry_pi_ip = '192.168.0.110'  # 라즈베리 파이의 IP 주소로 변경하세요
username = 'pi'                    # 라즈베리 파이의 사용자 이름
password = '48324832jh!'           # 라즈베리 파이의 비밀번호
python_script_path = '/home/pi/Desktop/raspProjects/servoMotorJetsonTest.py'  # 라즈베리 파이에서 서보 모터 제어 스크립트 경로

def send_command(command):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(raspberry_pi_ip, username=username, password=password)
        
        # 원격으로 파이썬 스크립트 실행
        stdin, stdout, stderr = client.exec_command(f'python3 {python_script_path} {command}')
        
        # 명령 실행 결과 출력
        print("Current Status : ", command)
        # for line in stdout:
        #     print(line.strip())
        # print("Error:")
        # for line in stderr:
        #     print(line.strip())
        
        # SSH 연결 종료
        client.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('/home/ubunt/Desktop/testCodes/gui_test.ui', self)

        # 적외선 카메라 제어 관련 요소 초기화
        self.ir_camera_view_widget = self.findChild(QWidget, 'ir_camera_view')
        self.ir_camera_view_layout = QVBoxLayout(self.ir_camera_view_widget)
        self.camera_viewer = CameraViewer()
        self.ir_camera_view_layout.addWidget(self.camera_viewer)
        self.camera_on_btn = self.findChild(QPushButton, 'camera_on_btn')
        self.camera_on_btn.clicked.connect(self.start_camera_stream)
        self.camera_off_btn = self.findChild(QPushButton, 'camera_off_btn')
        self.camera_off_btn.clicked.connect(self.stop_camera_stream)

        # 서보 모터 제어 관련 요소 초기화
        self.seed_bucket_open_btn = self.findChild(QPushButton, 'seed_bucket_open_btn')
        self.seed_bucket_open_btn.clicked.connect(self.start_servo)
        self.seed_bucket_close_btn = self.findChild(QPushButton, 'seed_bucket_close_btn')
        self.seed_bucket_close_btn.clicked.connect(self.stop_servo)

    def start_camera_stream(self):
        """
        카메라 스트리밍을 시작하는 메서드.
        """
        self.camera_viewer.start_camera()  # CameraViewer의 start_camera 메서드 호출

    def stop_camera_stream(self):
        """
        카메라 스트리밍을 중지하는 메서드.
        """
        self.camera_viewer.stop_camera()  # CameraViewer의 stop_camera 메서드 호출

    def start_servo(self):
        """
        서보 모터를 시작하는 메서드.
        """
        send_command('start')

    def stop_servo(self):
        """
        서보 모터를 중지하는 메서드.
        """
        send_command('stop')

def main():
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
