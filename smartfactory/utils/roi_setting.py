# opencv 라이브러리
import cv2

# 카메라 열기
cap = cv2.VideoCapture(0)

# 현재 카메라 해상도 얻기
width = cap.get(3)
height = cap.get(4)
print('default resolution width {} height {}'.format(width, height))

start_x = int(width / 2)
start_width = 30
start_y = 0
end_x = int(width / 2)
end_width = 160
end_y = height
c_r = (0, 0, 255)
thickness = 4

ROI = [190, 120, 350, 370]

x = ROI[0]
y = ROI[1]
w = ROI[2]
h = ROI[3]
if cap.isOpened():
    _, frame = cap.read()
else:
    _ = False


while _:

    _, frame = cap.read()

    key = cv2.waitKey(20)
    if key == 27:
        break
    else:
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, 'Your ROI', (x, y - 10), font, 1.3, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(w,h), c_r, thickness)
    cv2.imshow('', frame)


cap.release()
cv2.destroyAllWindows()

