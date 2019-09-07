# 轮廓发现：实际与图像边缘提取的基础寻找对象轮廓的方法。所以边缘提取的阈值选定会影响最终轮廓发现结果。
# API 发现轮廓：findContours     绘制轮廓：drawContours
# 代码知识点API的使用，掌握利用梯度来避免阈值烦恼


import cv2 as cv
import numpy as np


def contours_demo(image):
    # dst = cv.GaussianBlur(image, (3, 3), 0)        #这是二值图像的获取方法之一，与下面的并列
    # gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary image", binary)



    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # EXTERNAL只显示外轮廓，二TREE里面外面都显示
    for i, contour in enumerate(contours):           # 一个容器里面list循环
        cv.drawContours(image, contours, i, (0, 0, 255), 2)      # 最后一个参数是-1则填充
        print(i)
    cv.imshow("detect contours", image)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


contours_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()