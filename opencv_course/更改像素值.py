# numpy中fill的意思是将所有选中值填充成一个值
import cv2 as cv
import numpy as np


def access_pixels(image):       # 对所有像素进行访问(属性读取)
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s channels :%s"%(width, height, channels))
    for row in range(height):               # 进入循环，取图像的255-当前像素值
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255-pv
    cv.imshow("pixels_demo", image)


def inverse(image):     # opencv中取反的API
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():            # 该函数用于试着修改通道值


    # img = np.zeros([400, 400, 3], np.uint8)   # 多通道
    # # img[:, :, 0] = np.ones([400, 400])*255  # 修改通道0修改成灰度值255  蓝色
    # img[:, :, 2] = np.ones([400, 400]) * 255  # 修改通道2修改成灰度值255  红色
    # cv.imshow("new image", img)



    # # img = np.zeros([400, 400, 1], np.uint8)     # 单通道修改，将其值全部复位零（zero）
    # img = np.ones([400, 400, 1], np.uint8)        # 但通道值修都赋值为1更加方便，后面方便乘数
    # img = img*255
    # # img[:, :, 0] = np.ones([400, 400]) * 127
    # cv.imshow("new image", img)
    # cv.imwrite("C:/Users/11410/Desktop/save/myImage.png", img)

    m1 = np.ones([3, 3], np.uint8)
    m1.fill(122.388)
    print(m1)

    m2 = m1.reshape([1, 9])  # 讲解np中的reshape
    print(m2)


src = cv.imread("C:/Users/11410/Desktop/home.JPG")  # blue green red 三个通道
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
# create_image()
inverse(src)
t2 = cv.getTickCount()

time = (t2-t1)/cv.getTickFrequency()  # 这两句是计时，看扫描需要用多少秒
print("time : %s" % (time*1000))

access_pixels(src)
cv.waitKey(0)

cv.destroyAllWindows()