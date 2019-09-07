


import cv2 as cv
import numpy as np


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)





cv.waitKey(0)

cv.destroyAllWindows()