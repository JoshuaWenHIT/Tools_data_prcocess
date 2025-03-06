'''
单通道->三通道
'''
import os
import cv2
import numpy as np
import PIL.Image as Image
import os

# os.environ['CUDA_VISIBLE_DEVICES'] = '2'
img_path = '/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/RSD46-WHU/train (copy)/Airplane/'
save_img_path = '/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/RSD46-WHU/Airplane/'
for img_name in os.listdir(img_path):
    img = cv2.imread(img_path + img_name)
    if img.shape[2] == 1:  # 查看通道数
        # print(len(image.split()))
        # print(img_path + img_name)
        # im 为单通道图像  image为生成的三通道图像
        img = img[:, :, np.newaxis]
        image = img.repeat([3], axis=2)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img2 = np.zeros_like(img)
        # img2[:, :, 0] = gray
        # img2[:, :, 1] = gray
        # img2[:, :, 2] = gray
        cv2.imwrite(save_img_path + img_name, image)
        # image = Image.open(save_img_path + img_name)
        # print(len(image.split()))
    else:
        print("pass")


'''
单通道->三通道
'''
# img_src = np.expand_dims(img_src, axis=2)
# img_src = np.concatenate((img_src, img_src, img_src), axis=-1)
