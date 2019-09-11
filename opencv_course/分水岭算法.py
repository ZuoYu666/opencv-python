# 分水岭算法，分水岭变换介绍，opencv分水岭算法演示
# 距离变换，加个轮廓。
# 分水岭流程：输入图像--灰度--二值--距离变换--寻找种子--生成marker--分水岭变换--输出图像--end
# 分水岭算法实行之前，我们首先应当进行降噪处理

import cv2 as cv
import numpy as np


def watershed_demo(image):
    # remove noise if any
    print(src.shape)
    blurred = cv.GaussianBlur(image, (3, 3), 0)         # 终值滤波法用于边缘保留去噪
    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)     # 转灰度图
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化变量
    cv.imshow("binary-image", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 设置结构元素
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)       # 进行开操作
    sure_bg = cv.dilate(mb, kernel, iterations=3)  # 膨胀操作，将里面的小黑点点给填满了
    cv.imshow("mor-opt", sure_bg)

    # 先不管sure_bg，对mc进行距离变换
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)             # L2表示欧式距离
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)  # 输出距离变换结果，将结果标准化到0-1之间，这样能让结果很好的显示出来
    cv.imshow("distance-t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)    # 显示Mark位置
    cv.imshow("surface-bin", surface)
# 我觉得它时以圆心为起点向外辐射，做种子区域
    surface_fg = np.uint8(surface)              # 将最亮的区域转化为种子，变一个数据类型
    unknown = cv.subtract(sure_bg, surface_fg)     # 不知道的区域（种子区域出外的区域），为我们着色做准备的
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1             # 未知区域为255的区域都给设置成零
    markers[unknown==255] = 0
    markers = cv.watershed(src, markers=markers)      # 分水岭输出来的结果
    src[markers==-1] = [0, 0, 255]
    cv.imshow("result", src)


src = cv.imread("C:/Users/11410/opencv_code/opencv_exercises/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


watershed_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()

