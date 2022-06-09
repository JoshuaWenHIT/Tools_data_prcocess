import os
import cv2


image_format = ['.jpg', '.jpeg', '.png', '.tif', '.tiff', '.gif', '.bmp']


def image_convert(src_image_path, res_image_dir):
    img = cv2.imread(src_image_path, 1)
    image_name = src_image_path.split('/')[-1].split('.')[0]
    res_image_path = os.path.join(res_image_dir, (image_name + image_format[2]))
    cv2.imwrite(res_image_path, img)
    return res_image_path


if __name__ == '__main__':
    src_image_dir = '/home/joshuawen/Projects/Tools/data/image'
    res_image_dir = '/home/joshuawen/Projects/Tools/data/img_png'
    for root, dirs, files in os.walk(src_image_dir):
        for file in files:
            src_image_path = os.path.join(src_image_dir, file)
            res_list = image_convert(src_image_path=src_image_path, res_image_dir=res_image_dir)
            print(res_list)
