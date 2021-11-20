# 导入cv模块
import cv2 as cv

# 建立检测函数
def face_detect_demo():
    gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 加载分类器（opencv已经训练好可以直接用）
    face_detect=cv.CascadeClassifier('F:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face=face_detect.detectMultiScale(gary,1.01,5)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+w),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

img=cv.imread('233.jpg')
face_detect_demo()

# 等待，0的话就会一直等待下去
while True:
    if ord('q')==cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()