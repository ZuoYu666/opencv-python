# 超大图像二值化，我们将其进行局部阈值分割二值化，然后将它保存一个文件，在文件中分析查看，这样的效果比较好。

import cv2 as cv
import numpy as np


# def big_image_binary(image):
#     print(image.shape)
#     cw = 256
#     ch = 256
#     h, w = image.shape[:2]
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     for row in range(0, h, ch):
#         for col in range(0, w, cw):
#             roi = gray[row:row+ch, col:cw+col]
#             # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  #自动提取全局阈值会造成图像模糊
#             dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
# # 高斯局部分割法perfect，127那位必须式奇数。
#             gray[row:row + ch, col:cw + col] = dst
#             print(np.std(dst), np.mean(dst))
#     cv.imwrite("C:/Users/11410/Desktop/save/result_binary.png", gray)


def big_image_binary(image):   # 这个弄得全局阈值，将小于15的给转化成0了，起了过滤作用。
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:cw+col]
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:          # 小于15的去掉
                gray[row:row + ch, col:cw + col] = 255
            else :
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  #自动提取全局阈值会造成图像模糊
                # dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
    # 高斯局部分割法perfect，127那位必须式奇数。
                gray[row:row + ch, col:cw + col] = dst

    cv.imwrite("C:/Users/11410/Desktop/save/result_binary.png", gray)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/mnist_10k_sprite.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)


big_image_binary(src)


cv.waitKey(0)

cv.destroyAllWindows()