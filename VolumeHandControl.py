import cv2
import time
import HandTrackingModule as htm
import math
from subprocess import call

#########################
wCam, hCam = 640, 480   #
#########################
valid = False

cap = cv2.VideoCapture(0)
past_time = 0

detector = htm.HandDetector(detectionCon=0.5)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lm_list = detector.findPositions(img, draw=False)
    if len(lm_list) != 0:
        #  Coordinates
        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]
        x3, y3 = lm_list[12][1], lm_list[12][2]
        x4, y4 = lm_list[16][1], lm_list[16][2]
        x5, y5 = lm_list[20][1], lm_list[20][2]
        #  Circles
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x4, y4), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x5, y5), 15, (255, 0, 0), cv2.FILLED)
        #  Lines
        cv2.line(img, (x1, y1), (x2, y2), (255, 155, 255), 3)
        cv2.line(img, (x2, y2), (x3, y3), (255, 155, 255), 3)
        cv2.line(img, (x3, y3), (x4, y4), (255, 155, 255), 3)
        cv2.line(img, (x4, y4), (x5, y5), (255, 155, 255), 3)
        #  Length
        length1 = math.hypot(x2-x1, y2-y1)
        length2 = math.hypot(x3-x2, y3-y2)
        length3 = math.hypot(x4-x3, y4-y3)
        length4 = math.hypot(x5-x4, y5-y4)
        finally_length = length1 + length2 + length3 + length4
        max_length = 350
        volume_percents = (finally_length * 100)//max_length
        print(volume_percents)
        if finally_length < max_length:
            if (volume_percents <= 100) and (volume_percents >= 0):
                call(["amixer", "-D", "pulse", "sset", "Master", str(volume_percents) + "%"])
                valid = True
    current_time = time.time()
    fps = 1 / (current_time - past_time)
    past_time = current_time

    cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Volume Control With Hand", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break