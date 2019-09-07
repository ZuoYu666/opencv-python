#一维与多维

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot_demo(image):      #基于matplotlib的关于灰度值画直方图，它不是我们opencv想要的三通道直方图
    plt.hist(image.ravel(), 256, [0, 256])     #直接列表法统计
    plt.show("直方图")


def image_hist(image):      #图像的直方图,三个通道各自占每个像素值点的个数
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()



src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
plot_demo(src)
image_hist(src)

cv.waitKey(0)

cv.destroyAllWindows()