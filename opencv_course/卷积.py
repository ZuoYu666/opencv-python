# 学习目的，模糊操作，基于离散卷积，定义好每个卷积核，不同卷积核得到不同的卷积效果，模糊是卷积的一种现象
import cv2 as cv
import numpy as np


def blur_demo(image):        #进行了模糊，均值模糊，均值模糊的作用是取出随机噪声
    dst = cv.blur(image, (5, 5))  #定义卷积核
    cv.imshow("blur", dst)

def median_blur_demo(image):        #进行了模糊，中值模糊，中值模糊的作用是取出椒盐噪声
    dst = cv.medianBlur(image, 5)  #定义卷积核
    cv.imshow("blur", dst)

def custom_blur_demo(image):        #更加灵活的API，可以定义卷积核尺寸
    #kernel = np.ones([5, 5], np.float32)/25      #锐化算子
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)  #
    cv.imshow("blur", dst)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

#blur_demo(src)      #均值卷积
#median_blur_demo(src)  #中止卷积
custom_blur_demo(src)   #自定义卷积

cv.waitKey(0)

cv.destroyAllWindows()