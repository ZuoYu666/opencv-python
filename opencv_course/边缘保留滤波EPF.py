# 高斯双边，均值迁移。

import cv2 as cv
import numpy as np

                        # 高斯模糊是基于图像与空间的双模糊。
def bi_demo(image):     # 高斯双边模糊,保留图像边缘的模糊，也就是图像边缘收到的模糊程度很小，有着美艳滤镜的效果，且不改变部分文字内容。
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


def shift_demo(image):  # 均值迁移的方式作的，模糊程度大，但是缺点是有时会牵连边缘。
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

bi_demo(src)
shift_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()