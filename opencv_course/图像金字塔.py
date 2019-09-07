# 了解图像金字塔的原理，高斯金字塔与拉普拉斯金字塔
# reduce，先将原图像进行高斯模糊，然后进行各降采样（偶数行采样），一层一层递归。
# expand=扩大+卷积：高斯模糊+深采样，层层递归。小图expand-大图得到轮廓边界。

# g1-expand（g2），得到轮廓图
# 代码层面：pyrDown 降采样   PyrUp 还原


import cv2 as cv
import numpy as np


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_"+str(i), dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range (level-1, -1, -1):
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lpls_down_" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lpls_down_"+str(i), lpls)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


# pyramid_demo(src)
lapalian_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()