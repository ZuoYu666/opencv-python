


import cv2 as cv
import numpy as np


def face_detect_demo(image):
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("C:/Users/11410/opencv_code/face/face_tree.xml")
    faces = face_detector.detectMultiScale(image, 1.1, 2)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)



# src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/color_less.png")
capture = cv.VideoCapture(0)

# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)

    c = cv.waitKey(10)
    if c == 27:  # esc
        break

# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

face_detect_demo()

cv.waitKey(0)
cv.destroyAllWindows()