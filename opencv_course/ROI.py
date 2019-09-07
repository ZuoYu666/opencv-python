# ROI区域就是一幅图像人为选中的区域


import cv2 as cv
import numpy as np


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

face = src[25:225, 150:350]     #这几句话的含义是提取ROI区域（人脸），并提取灰度图
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[25:225, 150:350] = backface       #把改变后的RIO区域给还原回去了
cv.imshow("face", src)




cv.waitKey(0)

cv.destroyAllWindows()