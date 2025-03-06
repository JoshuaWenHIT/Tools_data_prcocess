import cv2
import numpy as np

img = cv2.imread('/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_res/method1/feature_map/layer0_conv1/channel_3.jpg')
# img = img[:, :, ::-1]
print(img.shape)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        R = img.item(x, y, 0)
        G = img.item(x, y, 1)
        B = img.item(x, y, 2)
        if R == 0 and G == 0 and B == 0:
            continue
        else:
            print('B: ', B)
            print('G: ', G)
            print('R: ', R)
            break
# x = 322
# y = 613
# # 打印这个图片（x,y）这个坐标的数值，0, 1, 2分别代表通道数，0代表Blue， 1代表Green， 2代表Red。
# R = img.item(x, y, 0)
# G = img.item(x, y, 1)
# B = img.item(x, y, 2)
# print('B: ', B)
# print('G: ', G)
# print('R: ', R)
# cv2.imwrite('/media/joshuawen/Data/video_det/YunCity/img/error_frame/2-res-rgb-000310.jpg', img)
