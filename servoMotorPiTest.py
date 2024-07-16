import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import paramiko

# 라즈베리 파이의 SSH 접속 정보
raspberry_pi_ip = '192.168.0.110'  # 라즈베리 파이의 IP 주소로 변경하세요
username = 'pi'                  # 라즈베리 파이의 사용자 이름
password = '48324832jh!'           # 라즈베리 파이의 비밀번호
python_script_path = '/home/pi/Desktop/raspProjects/servoMotorTest.py'  # 라즈베리 파이에서 서보 모터 제어 스크립트 경로

def send_command(command):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(raspberry_pi_ip, username=username, password=password)
        
        # 원격으로 파이썬 스크립트 실행
        stdin, stdout, stderr = client.exec_command(f'python3 {python_script_path} {command}')
        
        # 명령 실행 결과 출력
        print("Output:", command)
        # for line in stdout:
        #     print(line.strip())
        # print("Error:")
        # for line in stderr:
        #     print(line.strip())
        
        # SSH 연결 종료
        client.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('/home/ubunt/Desktop/testCodes/servoMotorTest.ui', self)

        # 버튼 클릭 시 연결할 메서드 설정
        self.startButton.clicked.connect(self.start_servo)
        self.stopButton.clicked.connect(self.stop_servo)

    def start_servo(self):
        send_command('start')

    def stop_servo(self):
        send_command('stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
