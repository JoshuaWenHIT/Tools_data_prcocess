# -*- coding: utf-8 -*-
import os
from shutil import copyfile, move


root_path = '/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/RSOD/pre'


def file_name(file_dir):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
            elif os.path.splitext(file)[1] == '.xml':
                xml_list.append(os.path.splitext(file)[0])

    diff1 = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print(len(diff1))
    for name in diff1:
        print("no jpg", name + ".xml")
        # copyfile(root_path + '\\xml\\' + name + '.xml', root_path + '\\xml_rest\\' + name + '.xml')
        move(root_path + '/annotations/' + name + '.xml', root_path + '/xml_rest/' + name + '.xml')

    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))
    for name in diff2:
        print("no xml", name + ".jpg")
        # copyfile(root_path + '\\image\\' + name + '.jpg', root_path + '\\image_rest\\' + name + '.jpg')
        move(root_path + '/images/' + name + '.jpg', root_path + '/image_rest/' + name + '.jpg')

    return jpg_list, xml_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名


if __name__ == '__main__':

    file_name(root_path)
