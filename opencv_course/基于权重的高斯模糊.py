import cv2 as cv
import numpy as np


def clamp(pv):          #写一个函数，确保像素灰度值在0-255之间
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape        #写一个噪声图像，它的维度和原图像一样
    for row in range(h):         #逐行列扫描
        for col in range(w):
            s = np.random.normal(0, 20, 3)  #
            b = image[row, col, 0]  #blue
            g = image[row, col, 1]  #green
            r = image[row, col, 2]  #red

            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(b + s[1])
            image[row, col, 2] = clamp(b + s[2])
    cv.imshow("noise image", image)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


                        #计算gaussian_noise所消耗的时间
t1 = cv.getTickCount()    #初始时间
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time consume %s"%(time*1000))         #打印时间，它的格式是以毫秒为单位

dst = cv.GaussianBlur(src, (5, 5), 15)  #这是高斯模糊的API
cv.imshow("Gaussian Blur", dst)          #高斯模糊对高斯噪声有抑制作用

cv.waitKey(0)

cv.destroyAllWindows()