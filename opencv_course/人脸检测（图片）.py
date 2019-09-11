


import cv2 as cv
import numpy as np


def face_detect_demo():
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("C:/Users/11410/opencv_code/face/face_tree.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 2)
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", src)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/color_less.png")

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

cv.imshow("input image", src)

face_detect_demo()

cv.waitKey(0)
cv.destroyAllWindows()