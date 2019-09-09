# 直线检测，圆检测都是基于霍夫变换。


import cv2 as cv
import numpy as np


def line_detection(image):          #直线检测
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)        #霍夫直线检测（边缘，起始半径1，角度步长1度，边缘提取的地址的低值）
    for line in lines:
        rho, theta = line[0]           #r的步长，theta的步长
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image-lines", image)


def line_detect_possible_demo(image):      # 存储多为数组API由cv.HoughLines换成了cv.HoughLinesP，代码便间接了不少，免去了手动写迭代
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=1)  #API最后两个参数（最短线长，能容忍断的最大像素点）
    for line in lines:
        print(type(line))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_possible_demo", image)

src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/image_lines.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


line_detection(src)

line_detect_possible_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()