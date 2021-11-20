# 导入cv模块
import cv2 as cv
# 读取图片
img=cv.imread('face1.jpg')

# 修改尺寸
resize_img=cv.resize(img,dsize=(200,200))
# 显示原图
cv.imshow('img',img)
# 显示修改后的图
cv.imshow('resize_img',resize_img)
# 打印各自的尺寸
print('未修改的尺寸：',img.shape)
print('修改后的尺寸：',resize_img.shape)

# 等待，0的话就会一直等待下去
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()