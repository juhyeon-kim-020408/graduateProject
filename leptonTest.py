import cv2
import numpy as np

# 비디오 캡처 열기
cameraID = 0
vc = cv2.VideoCapture(cameraID)

# 카메라가 성공적으로 열렸는지 확인
if not vc.isOpened():
    print("Error: Could not open camera.")
    exit()

# 화재 감지 임계값
FIRE_THRESHOLD = 1  # 실제 온도에 맞게 조정 필요


# 프레임에서 화재를 확인하는 함수
def detect_fire(frame):
    # 프레임을 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # min_temp = np.min(gray)
    print("gray 값 :", gray)

    # 최대 온도 값이 화재 임계값을 초과하는지 확인
    # if min_temp > FIRE_THRESHOLD:
    #     return True
    # return False


# 메인 루프
while True:
    rval, frame = vc.read()
    if not rval:
        break

    # 프레임에서 화재 확인
    if detect_fire(frame):
        print("Fire detected!")

    else:
        print("화재 감지 중...")

    # # 프레임을 정규화하여 보기 좋게 변경
    # frame_normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
    # frame_normalized = np.uint8(frame_normalized)

    # # 프레임을 컬러맵으로 변환하여 표시
    # frame_colormap = cv2.applyColorMap(frame_normalized, cv2.COLORMAP_JET)
    cv2.imshow("preview", frame)

    if cv2.waitKey(20) & 0xFF == 27:
        break

# 비디오 캡처 해제 및 창 닫기
vc.release()
cv2.destroyAllWindows()


