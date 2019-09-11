# 开操作开闭操作时形态学的重要操作，基于膨胀与腐蚀的组合操作。主要时应用在二至图像分析中，灰度图像也可以。开操作=腐蚀+膨胀，输入图像+结构元素
# 闭操作=膨胀+腐蚀，输入图像+结构元素
# 开操作作用：取出小的干扰快。  比操作作用：填充闭合区域。  水平或者直线的提取。

import cv2 as cv
import numpy as np


def open_demo(image):          # 开操作
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 得到二值图像
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))    # 保留横线，去掉竖线
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


def close_demo(image):          # 闭操作
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 得到二值图像
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (100, 100))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close-result", binary)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/result_big_image.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

open_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()