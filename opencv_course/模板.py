


import cv2 as cv
import numpy as np

def face_detect_demo():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier()
    faces = face_detector.detectMultiScale(gray, 1.62, 5)
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("face_detect_demo", src)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

cv.namedWindow("result", cv.WINDOW_AUTOSIZE)



cv.waitKey(0)

cv.destroyAllWindows()