# 学习要求 HSV与RGB色彩空间，反向投影相关API，掌握反向投影应用场合
# 可用于目标物体的跟踪


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def back_projection_demo():       # 紫色的部分都出来了
    sample = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/sample.png")
    target = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)          #归一化操作
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


def hist2d_demo(image):        #建立2维直方图  在HSV空间上
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

hist2d_demo(src)
# back_projection_demo()

cv.waitKey(0)

cv.destroyAllWindows()
