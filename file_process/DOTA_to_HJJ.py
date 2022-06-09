import os
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
    return list


def txt_concat(dir_path):
    txt_list = {}
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            cls = name.split('.')[0].split('_')[1]
            cls = str(cls)
            txt_list_sub = read_txt_to_list(os.path.join(dir_path, name))
            txt_list_sub = txt_list_sub[:-1]
            txt_list[cls] = txt_list_sub
            # txt_list[cls].append(txt_list_sub)
            txt_list[cls].sort()
    return txt_list


def txt_to_HJJ(txt_list, results_path):
    results_txt = open(results_path + '/HJJ_results.txt', 'w')
    for cls in txt_list:
        for object in txt_list[cls]:
            name = object.split(' ')[0] + ' '
            results_txt.write(name)
            conf = np.float32(object.split(' ')[1])
            results_txt.write(str(conf))
            results_txt.write(' ')
            x1 = object.split(' ')[2]
            if np.float32(x1) >= 0:
                print(x1)
                x1 = int(str(x1 + 0.5))
            else:
                x1 = int(str(x1 - 0.5))
            results_txt.write(str(x1))
            results_txt.write(' ')
            y1 = object.split(' ')[3]
            if np.float32(y1) >= 0:
                y1 = int(str(y1 + 0.5))
            else:
                y1 = int(str(y1 - 0.5))
            results_txt.write(str(y1))
            results_txt.write(' ')
            x2 = object.split(' ')[4]
            if np.float32(x2) >= 0:
                x2 = int(str(x2 + 0.5))
            else:
                x2 = int(str(x2 - 0.5))
            results_txt.write(str(x2))
            results_txt.write(' ')
            y2 = object.split(' ')[5]
            if np.float32(y2) >= 0:
                y2 = int(str(y2 + 0.5))
            else:
                y2 = int(str(y2 - 0.5))
            results_txt.write(str(y2))
            results_txt.write(' ')
            x3 = object.split(' ')[6]
            if np.float32(x3) >= 0:
                x3 = int(str(x3 + 0.5))
            else:
                x3 = int(str(x3 - 0.5))
            results_txt.write(str(x3))
            results_txt.write(' ')
            y3 = object.split(' ')[7]
            if np.float32(y3) >= 0:
                y3 = int(str(y3 + 0.5))
            else:
                y3 = int(str(y3 - 0.5))
            results_txt.write(str(y3))
            results_txt.write(' ')
            x4 = object.split(' ')[8]
            if np.float32(x4) >= 0:
                x4 = int(str(x4 + 0.5))
            else:
                x4 = int(str(x4 - 0.5))
            results_txt.write(str(x4))
            results_txt.write(' ')
            y4 = object.split(' ')[9]
            if np.float32(y4) >= 0:
                y4 = int(str(y4 + 0.5))
            else:
                y4 = int(str(y4 - 0.5))
            results_txt.write(str(y4))
            results_txt.write('\n')


if __name__ == '__main__':
    dota_results_path = '/home/joshuawen/Projects/Tools/data/'
    results_path = '/home/joshuawen/Projects/Tools/data'
    txt_list = txt_concat(dota_results_path)
    txt_to_HJJ(txt_list, results_path)