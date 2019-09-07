# 直方图用处很多，可以调整对比度，对图像进行直方图均衡化，直方图比较
# 巴氏距离，相关性，卡方
import cv2 as cv
import numpy as np


def equalHist_demo(image):  #整体的直方图均衡化，增强了图像的对比度
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):      #直方图局部均衡化，可调
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)

def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴士距离: %s, 相关性: %s, 卡方:%s"%(match1, match2, match3))


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

# equalHist_demo(src)  # 整体均衡化
clahe_demo(src)        # 局部均衡化



# 输入两张图像，对它们进行直方图比较

image1 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")
image2 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/02.jpg")
cv.imshow("image1", image1)
cv.imshow("image2", image2)

hist_compare(image1, image2)



cv.waitKey(0)

cv.destroyAllWindows()