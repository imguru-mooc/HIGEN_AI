import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 40)

FPS = cap.get(cv2.CAP_PROP_FPS)

if FPS ==0:
    FPS =30

W = int(cap.get(3))
H = int(cap.get(4))

REC_TIME_SEC = 120
REC_FILE_NAME = 'factory.mp4'
FRAME_CNT = 0
print(FPS)

print('width :%d, height : %d' % (W, H))
video_out = cv2.VideoWriter('SAVE/' + REC_FILE_NAME, cv2.VideoWriter_fourcc(*'DIVX'), FPS, (W, H))

while (cap.isOpened()):
    try:
        # Capture frame by frame
        ret, frame = cap.read()

        # Save
        cv2.imshow('',frame)
        video_out.write(frame)

        FRAME_CNT = FRAME_CNT + 1
        if FRAME_CNT >= FPS * REC_TIME_SEC:
            print('Stop recording for {} seconds'.format(REC_TIME_SEC))
            break

        if (FRAME_CNT % FPS) == 0:
            print('Recording.. {:.2f}%'.format((100 * FRAME_CNT) / (REC_TIME_SEC * FPS)))

    except KeyboardInterrupt:  # input the 'ii' key
        break

video_out.release()
cap.release()
cv2.destroyAllWindows()
