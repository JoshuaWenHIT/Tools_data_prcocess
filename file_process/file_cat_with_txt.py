import os
import shutil


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


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件
        print("move %s -> %s" % (srcfile, dstfile))


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def match_dir_with_list(src_dir_path, list, dst_dir_path):
    for root, dirs, files in os.walk(src_dir_path, topdown=True):
        for name in files:
            pre, ending = os.path.splitext(name)
            if pre in list:
                mycopyfile(os.path.join(root, name), os.path.join(dst_dir_path, name))


if __name__ == "__main__":
    txt_path = "/media/joshuawen/Datasets/Datasets/ships/train/Main/val.txt"
    src_dir_path = "/media/joshuawen/Datasets/Datasets/ships/train/xml"
    dst_dir_path = "/media/joshuawen/Datasets/Datasets/ships/train/xml_val"

    filename_list = read_txt_to_list(txt_path=txt_path)
    print(len(filename_list))
    print(filename_list)
    match_dir_with_list(src_dir_path=src_dir_path, list=filename_list, dst_dir_path=dst_dir_path)
