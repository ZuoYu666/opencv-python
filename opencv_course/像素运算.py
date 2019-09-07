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

def contrast_brightness_demo(image, c, b):
    h, w, h = image.shape[: 2]
    blank = np.zeros([h, w, ch], image.dtype)       #创建一个维度相同的零像素图片
    cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)


def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)   #这是个测方差的函数
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)


    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


def logic_demo(m1, m2):      # 逻辑运算
    # dst = cv.bitwise_and(m1, m2)  # 与
    # dst = cv.bitwise_or(m1, m2)   # 或
    dst = cv.bitwise_not(m1, m2)  # 非
    cv.imshow("logic_demo", dst)


src1 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")
src2 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/02.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
# cv.namedWindow("image2", cv.WINDOW_AUTOSIZE)
#src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")
#cv.imshow("image1", src1)
#cv.imshow("image2", src2)
#add_demo(src1, src2)
#subtract_demo(src1, src2)
#multiply_demo(src1, src2)
#divide_demo(src1, src2)
#others(src1, src2)



# logic_demo(src1, src2)


cv.imshow("image1", src1)
cv.imshow("image2", src2)

src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")
# add_demo(src1, src2)
cv.imshow("image2", src)
contrast_brightness_demo(src, 1.2, 10)

cv.waitKey(0)
cv.destroyAllWindows()