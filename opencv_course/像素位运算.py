#学习目的：像素运算，（算术运算、逻辑运算）常见的图像混合、
#加减乘除可用于调整对比度亮度
import cv2 as cv
import numpy as np


def add_demo(m1, m2):      # 两幅图片进行加运算
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)

def subtract_demo(m1, m2):  # 两幅图片进行间运算
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def multiply_demo(m1, m2):      # 两幅图片进行乘运算
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def divide_demo(m1, m2):      # 两幅图片进行除运算
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def other(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)      #返回值 均值、标准差
    M2, dev2 = cv.meanStdDev(m2)

    h, w = m1.shape[:2]                #定义高、宽变量与m1相同

    print(M1)      #打印src1的均值
    print(M2)
    print(dev1)    #打印src1的标准差
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


src1 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")  # 定义变量1是01图片
src2 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/02.jpg")  # 定义变量2是02图片
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)

cv.imshow("image1", src1)
cv.imshow("image2", src2)

add_demo(src1, src2)
subtract_demo(src1, src2)
multiply_demo(src1, src2)
divide_demo(src1, src2)
other(src1, src2)

cv.waitKey(0)

cv.destroyAllWindows()