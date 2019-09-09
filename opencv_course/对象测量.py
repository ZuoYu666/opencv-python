# 目的，得到字或图像的外接矩形
# 了解多边逼近函数


import cv2 as cv
import numpy as np


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)       #二值化过程
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value : %s" % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)

    contours, hireachy, = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h) / max(w, h)
        print("rectangle_rate : %s"% rate)
        mm = cv.moments(contour)  # moments中心矩，可以求面积、质心
        print(type(mm))
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area %s"%area)        # 打印每个字外面方框所占的面积

        approxCurve = cv.approxPolyDP(contour, 6, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 2:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)

        if approxCurve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (255, 0, 0), 2)

        if approxCurve.shape[0] == 3:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)

    cv.imshow("measure-contours", dst)




src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/circle_detection.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

measure_object(src)


cv.waitKey(0)

cv.destroyAllWindows()