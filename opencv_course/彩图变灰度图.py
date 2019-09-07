import cv2 as cv
import numpy as np
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        cv.imshow("video", frame)
        c = cv.waitKey(50)  # 响应用户操作50ms
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image);
    print(pixel_data)


src = cv.imread("C:/Users/11410/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
#cv.imwrite("C:/Users/11410/Desktop/save/cai.png", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("C:/Users/11410/Desktop/save/huidu.png", gray)
# video_demo()
cv.waitKey(0)

cv.destroyAllWindows()


