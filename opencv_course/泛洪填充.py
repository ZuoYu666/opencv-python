# ROI区域就是一幅图像人为选中的区域


import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)        # 注意，只有这样维度的矩阵才能进行mask操作
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    # 上面那句话表示图像填充，里面都是API的参数，可以到网上找一个例子看看，最后一个参数是惯例，彩色图像一般都用这个
    cv.imshow("fill_color_demo", copyImg)

def fill_binary_demo(image):

    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_color_demo", image)

    mask = np.ones([402, 402, 1], np.uint8)     # 带mask都与二值图像有关，填充是，应把空白区域都初始化为1
    mask[101:301, 101:301] = 0                  # 为0的区域才能被填充
    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)

src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

#fill_color_demo(src)
fill_binary_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()