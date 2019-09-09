# 多变形拟合，获取轮廓的多边形拟合结果，approxPolyDP，-contour，-epsilon越小越折线逼近真实形状，-close-是否位闭合区域

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
    edge_output = cv.Canny(gray, 50, 150)                 # 这个是直接把灰度图扔里面了，它将会自动提取梯度，后两个参数和轮廓能否提取有关

    cv.imshow("Canny Edge", edge_output)                  # 获得的黑白边缘

    return edge_output


def contours_demo(image):
    binary = edge_demo(image)
    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # EXTERNAL只显示外轮廓，二TREE里面外面都显示
    for i, contour in enumerate(contours):           # 一个容器里面list循环
        cv.drawContours(image, contours, i, (0, 0, 255), 2)      # 最后一个参数是-1则填充
        print(i)
    cv.imshow("detect contours", image)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


contours_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()