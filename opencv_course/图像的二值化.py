# 知识点：Opencv中图像二值化方法，
# 图像的二值化函数  OTSU、Triangle、自动与手动、自适应阈值

import cv2 as cv
import numpy as np


def threshold_demo(image):           #图像的二值化函数
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret , binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 自动阈值寻找的全局二值化根据阈值二值化，直方图由多个波峰波谷式用它
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)  # 自动阈值寻找的全局二值化根据阈值二值化，直方图由单个波峰用它
    # ret, binary = cv.threshold(gray, 127, 125, cv.THRESH_BINARY)  #自定义阈值的二值化操作
    # ret, binary = cv.threshold(gray, 127, 125, cv.THRESH_BINARY_INV)  #自定义阈值，黑白取反的二值化操作
    # ret, binary = cv.threshold(gray, 127, 125, cv.THRESH_TRUNC)  #截断式二值化
    # ret, binary = cv.threshold(gray, 127, 125, cv.THRESH_TOZERO)  #小于阈值都变零，大于阈值都等于阈值
    print("threshold cvlue %s"%ret)
    cv.imshow("binary", binary)


def local_threshold(image):    # 基于局部阈值的二值化图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10) #cmeans法
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10) #高斯means
    cv.imshow("binary", binary)



def custom_threshold(image):               #用整体均值分割
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])  #m等于gray展开的一维数组
    mean = m.sum() / (w*h)
    print("mean :", mean)
    RET, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# threshold_demo(src)
#local_threshold(src)
custom_threshold(src)

cv.waitKey(0)

cv.destroyAllWindows()