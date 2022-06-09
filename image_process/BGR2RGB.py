import cv2
import os
from pathlib import Path


def BGR2RGB(bgr_img_path, rgb_img_path):
    bgr_img = cv2.imread(bgr_img_path)
    b, g, r = cv2.split(bgr_img)
    rgb_img = cv2.merge([r, g, b])
    # cv2.imwrite(rgb_img_path, rgb_img[100:620, 0:1920])
    cv2.imwrite(rgb_img_path, rgb_img[70:650, 0:1280])


def images_process(ori_dir, tar_dir):
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    for img_name in os.listdir(ori_dir):
        ori_img_path = os.path.join(ori_dir, img_name)
        tar_img_path = os.path.join(tar_dir, img_name)
        BGR2RGB(ori_img_path, tar_img_path)
        print("{} is transformed into {}".format(ori_img_path, tar_img_path))


if __name__ == '__main__':
    # ori_dir = "/media/joshuawen/Data/video_det/YunCity/video/original/img"
    # tar_dir = "/media/joshuawen/Data/video_det/YunCity/video/original/img_rgb"
    # images_process(ori_dir=ori_dir, tar_dir=tar_dir)
    orig_img = "/media/joshuawen/Data/video_det/JiaHe/error_frame/000569.jpg"
    res_img = "/media/joshuawen/Data/video_det/JiaHe/error_frame/000569_res.jpg"
    BGR2RGB(bgr_img_path=orig_img, rgb_img_path=res_img)