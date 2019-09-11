# 顶帽，黑帽，形态学梯度，代码层面知识
# 顶帽，源图像 与开操作之间的差值图像
# 黑帽，比图像与源图像的差值图像
# 形态梯度：用膨胀后的图像减去腐蚀后的图像得到的差值图像。把用此方法得到的梯度称为基本梯度
# 内部梯度：是原图像减去夫时候的图像得到的差值图像。
# 外部梯度：图像膨胀后再减去原来的图像得到的差值图像。

import cv2 as cv
import numpy as np


def top_hat_demo(image):          # 顶帽操作（灰度图像得出的结果）
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      # 灰度值
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 构造结构元素
    # dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)  # 顶帽  腐蚀完再膨胀
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)    #黑帽法提取轮廓
    cimage = np.array([gray.shape, np.uint8])
    cimage = 100
    dst = cv.add(dst, cimage)
    cv.imshow("tophat", dst)


# 由此可看出，丁茂操作可以操作将单独封闭区域的点提取出来
def top_binary_demo(image):          # 顶帽操作(二值图像得出的结果)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      # 灰度值
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 构造结构元素
    # dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)  # 顶帽  腐蚀完再膨胀
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)    #黑帽法提取轮廓
    cv.imshow("tophat", dst)


def extract_gradient_demo(image):          # 梯度操作(二值图像得出的结果)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      # 灰度值
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 构造结构元素
    # dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)  # 顶帽  腐蚀完再膨胀
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)    # 黑帽法提取轮廓
    cv.imshow("gradient", dst)


def i_o_gradient_demo(image):          # 内/外梯度操作(二值图像得出的结果)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 构造结构元素
    dm = cv.dilate(image, kernel)         # 内梯度
    em = cv.erode(image, kernel)          # 外梯度
    dst1 = cv.subtract(image, em)       # internol_grodient(内梯度）
    dst2 = cv.subtract(dm, image)       # externol_gradient
    cv.imshow("internol_gradient", dst1)
    cv.imshow("externol_gradient", dst2)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/binary_image.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


# top_binary_demo(src)
# top_hat_demo(src)
# extract_gradient_demo(src)
i_o_gradient_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()