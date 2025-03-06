import os
import cv2


img_dir = '/media/joshuawen/Datasets/Datasets/ships/train/pic'
h_max = 0
h_min = 100000
w_max = 0
w_min = 100000
for img_name in sorted(os.listdir(img_dir)):
    print(img_name)
    img = cv2.imread(os.path.join(img_dir, img_name))
    w = img.shape[0]
    h = img.shape[1]
    if w > w_max:
        w_max = w
    if h > h_max:
        h_max = h
    if w < w_min:
        w_min = w
    if h < h_min:
        h_min = h

print('w_max: ', w_max)
print('h_max: ', h_max)
print('w_min: ', w_min)
print('h_min: ', h_min)
