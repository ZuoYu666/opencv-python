# 图像梯度，异界倒数与soble算子，二阶导数与拉普拉斯算子
# 无论式sobel算子，还是拉普拉斯算子，其矩阵代数和都是零，普通的算子式四邻域的，增强型的算子是八邻域的。


import cv2 as cv
import numpy as np


def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)     # 在x方向进行一阶导数求算
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)     # 在y方向进行一阶导数求算

    # grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)  # 在x方向进行一阶导数求算(类似于sobel算子的另一个算子)
    # grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)  # 在y方向进行一阶导数求算


    gradx = cv.convertScaleAbs(grad_x)            # 在x方向扫描边界轮廓
    grady = cv.convertScaleAbs(grad_y)            # 在y方向扫描边界轮廓
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


def lapalian_demo(image):               #通过拉普拉斯算子进行卷积
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)

def lapalian_demo1(image):               #自定义卷积算子进行卷积
    kernel = np.array([[0, 1,0], [1, -4, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# sobel_demo(src)

lapalian_demo1(src)

cv.waitKey(0)

cv.destroyAllWindows()