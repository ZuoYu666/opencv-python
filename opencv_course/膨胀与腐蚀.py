# 腐蚀，膨胀，相关API代码演示
# 关于形态学的知识




import cv2 as cv
import numpy as np


def erode_demo(image):         # 腐蚀操作
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.erode(binary, kernel)
    cv.imshow("binary", binary)
    cv.imshow("ecode_demo", dst)


def dilate_demo(image):         # 腐蚀操作
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.dilate(binary, kernel)
    cv.imshow("binary", binary)
    cv.imshow("dilate_demo", dst)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/erode_and_dilate.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


erode_demo(src)
dilate_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()