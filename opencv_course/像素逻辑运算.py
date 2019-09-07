#学习目的：像素运算，（算术运算、逻辑运算）常见的图像混合、
#加减乘除可用于调整对比度亮度



#小技巧------赋值宽和高，python可以一行设置两个返回值，而后面是数组，非常方便
import cv2 as cv
import numpy as np


def logic_demo(m1, m2):
    #dst = cv.bitwise_and(m1, m2)     # 逻辑与
    dst = cv.bitwise_or(m1, m2)       # 或
    #dst = cv.bitwise_not(m1, m2)     # 非
    cv.imshow("logic_demo", dst)

def contrast_brightness_demo(image, c, b):      #该函数用于更改函数对比度  c表示对比度，b表示亮度

    h, w, ch = image.shape               #这两句话的含义就是创造一个空白图像，长宽和通道个数和image一样
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)    #调整图像的对比度
    cv.imshow("con-bri-demo", dst)

def other(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)      #返回值 均值、标准差
    M2, dev2 = cv.meanStdDev(m2)

    h, w = m1.shape[:2]                #定义高、宽变量与m1相同

    print(M1)      #打印src1的均值
    print(M2)
    print(dev1)    #打印src1的标准差
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


src1 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/01.jpg")  # 定义变量1是01图片
src2 = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/02.jpg")  # 定义变量2是02图片
#cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)

#cv.imshow("image1", src1)
#cv.imshow("image2", src2)

#logic_demo(src1, src2)
src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.imshow("image2", src)
contrast_brightness_demo(src, 1.2, 50)  # 入口参数，图片、对比度、亮度

cv.waitKey(0)

cv.destroyAllWindows()