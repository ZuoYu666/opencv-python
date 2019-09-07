#用户hdv追踪有颜色的对象
import cv2 as cv
import numpy as np

def extrace_object_demo():
    capture = cv.VideoCapture("C:/Users/11410/python代码/opencv_exercises/images/Crystal.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_hsv = np.array([26, 43, 46])             # 过滤那个颜色需要查表（低值）,这个例子是提取黄色
        upper_hsv = np.array([64, 255, 255])           # （高值）

        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  # API  inrange它是过滤颜色的主角  mask通常表示二值图像
        dst = cv.bitwise_and(frame, frame, mask=mask)  #dst表示捕捉的特定颜色的照片

        cv.imshow("video", frame)
        #cv.imshow("mask", mask)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c== 27:
            break


def color_space_demo(image):     # 空间模型转换，RGB转HSV或YUV
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrch", ycrcb)


src = cv.imread("C:/Users/11410/Desktop/home.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

extrace_object_demo()
color_space_demo(src)


b, g, r = cv.split(src)  #通道分离操作
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

src[:, :, 0] = 0  # 将最后一个通道(红色通道)赋为零
cv.imshow("changed image", src)
src = cv.merge([b, g, r])

cv.waitKey(0)

cv.destroyAllWindows()