import os

import cv2
import numpy as np

IMG_DIR = "/home/HDD/Datasets/UAV/VisDrone/SOT/VisDrone2019-SOT-val/sequences/uav0000317_00000_s_interfere"
IMG_NAME = "img0000201.jpg"
RES_DIR = "/home/HDD/Datasets/UAV/VisDrone/SOT/VisDrone2019-SOT-val/sequences/uav0000317_00000_s_interfere_res"

# image = cv2.imread(os.path.join(IMG_DIR, IMG_NAME))
# h, w, _ = image.shape
# mask = np.zeros((h, w), dtype=np.uint8)
# start_x = 0
# end_x = start_x + 1000
# start_y = 0
# end_y = start_y + 1000
# # mask[start_y: end_y, start_x: end_x] = (255, 255, 255)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # result = cv2.bitwise_and(image, mask) / 255 * gray_image
# # result = cv2.bitwise_and(image, mask)
# result = image
# result[start_y: end_y, start_x: end_x] = (127, 127, 127)
#
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def add_interfere(image, start_x, start_y, ex_x, ex_y, color=(127, 127, 127)):
    h, w, _ = image.shape
    end_x = start_x + ex_x
    end_y = start_y + ex_y
    image[start_y: end_y, start_x: end_x] = color
    return image


if __name__ == '__main__':
    img_list = sorted(os.listdir(IMG_DIR))
    start_index = 200
    end_index = 300
    for img in img_list[200: 300]:
        image = cv2.imread(os.path.join(IMG_DIR, img))
        img_interfere = add_interfere(image, start_x=1000, start_y=0, ex_x=200, ex_y=1070)
        cv2.imwrite(os.path.join(RES_DIR, img), img_interfere)
        print("Done")
