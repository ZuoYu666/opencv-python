# 圆检测  圆边缘个点投影到霍夫曼空间，边缘点位置交于一点，该点则为霍夫曼域的圆心


import cv2 as cv
import numpy as np


def detect_circle_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=5, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("circles", image)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


detect_circle_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()