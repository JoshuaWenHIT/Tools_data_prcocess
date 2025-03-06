import os
import cv2
import numpy as np


def read_txt_to_list(txt_path):
    list = []
    f = open(txt_path, "r")  # 设置文件对象
    line = f.readline()
    # print(line)
    line = line.strip('\n')
    list.append(line)
    while line:  # 直到读取完文件
        line = f.readline()  # 读取一行文件，包括换行符
        line = line.strip('\n')  # 去掉换行符，也可以不去
        list.append(line)
    f.close()
    # print(list)
    return list


def draw_box(list):
    for ins in list[:-1]:
        img_name = ins.split(' ')[0]
        cls = ins.split(' ')[1]
        conf = ins.split(' ')[2]
        x1 = ins.split(' ')[3]
        y1 = ins.split(' ')[4]
        x2 = ins.split(' ')[5]
        y2 = ins.split(' ')[6]
        x3 = ins.split(' ')[7]
        y3 = ins.split(' ')[8]
        x4 = ins.split(' ')[9]
        y4 = ins.split(' ')[10]
        img = cv2.imread(os.path.join('/home/joshuawen/Projects/Tools/data/image', img_name))
        xy_set = [[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]]
        cv2.polylines(img, np.array(xy_set, dtype=np.int32), 2, (50, 205, 50))
        cv2.putText(img, cls, (int(x1), int(y1)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (60, 20,220 ), 1, cv2.LINE_AA)
        cv2.putText(img, conf, (int(x1), int(y1) + 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imwrite(os.path.join('/home/joshuawen/Projects/Tools/data/image', img_name), img)
        print('{} is visualized !'.format(img_name))
        # cv2.imshow('img_results', img)
        # cv2.waitKey(0)


if __name__ == '__main__':
    txt_list = read_txt_to_list('/home/joshuawen/Projects/Tools/data/results.txt')
    draw_box(txt_list)
