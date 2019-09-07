# canny边缘提取， canny算法介绍，
# 步骤及详情在word笔记上。


import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)      #高斯降噪
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # X Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)                 #这个是直接把灰度图扔里面了，它将会自动提取梯度

    cv.imshow("Canny Edge", edge_output)                  #获得的黑白边缘

    dst = cv.bitwise_and(image, image, mask=edge_output)  #获得的彩色边缘
    cv.imshow("Color Edge", dst)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


edge_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()