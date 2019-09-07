import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/subpixel5.png")
    target = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/1.png")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  #方法（0-1，相关性的，相关性因子的）
    th, tw = tpl.shape[:2]     #设置模板的高，宽，设置三通道的前两个维度
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md  == cv.TM_CCOEFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        # cv.imshow("match-"+np.str(md), target)
        cv.imshow("match-"+np.str(md), result)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/a_zhu.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

template_demo()


cv.waitKey(0)

cv.destroyAllWindows()