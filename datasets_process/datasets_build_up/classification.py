#
#  classification.py
#  datasets_build_up
#
#  Created by Joshua Wen on 2022/06/08.
#  Copyright © 2022 Joshua Wen. All rights reserved.
#
import os
import shutil
import random
from PIL import Image


class ClassificationDatasetsStatistic:
    def __init__(self, dir_path):
        self.path = dir_path
        self.format_list = ['png', 'jpg', 'jpeg', 'tif', 'tiff', 'bmp']
        self.class_dict = dict()
        self.res_dict = dict()
        self.res_set = set()
        self.format_dict = dict()

    def main(self):
        for root, dirs, files in os.walk(self.path, topdown=True):
            if not files:
                self.class_dict = dict(zip(dirs, [0] * len(dirs)))
            else:
                file_number = 0
                for file in files:
                    file_format = file.split('.')[-1]
                    if file_format not in self.format_list:
                        print("{} is not an image !".format(file))
                        continue
                    else:
                        file_number += 1
                        print("\rprocessing... : {}".format(file), end='')

                        if file_format not in self.format_dict.keys():
                            self.format_dict[file_format] = 1
                        else:
                            self.format_dict[file_format] += 1

                        img_size = Image.open(os.path.join(root, file)).size
                        self.res_set.add(img_size)
                        if img_size not in self.res_dict.keys():
                            self.res_dict[img_size] = 1
                        else:
                            self.res_dict[img_size] += 1
                self.class_dict[root.split('/')[-1]] = file_number
        self.res_dict = sorted(self.res_dict.items(), key=lambda x: x[1], reverse=True)

    def get_class(self):
        for root, dirs, files in os.walk(self.path, topdown=True):
            if not files:
                self.class_dict = dict(zip(dirs, [0] * len(dirs)))
            else:
                self.class_dict[root.split('/')[-1]] = len(files)

    def get_resolution(self):
        for root, dirs, files in os.walk(self.path, topdown=True):
            if files:
                for file in files:
                    if file.split('.')[-1] not in self.format_list:
                        print("{} is not an image !".format(file))
                        continue
                    else:
                        print("\rresolution calculate: {}".format(file), end='')
                        img_size = Image.open(os.path.join(root, file)).size
                        self.res_set.add(img_size)
                        if img_size not in self.res_dict.keys():
                            self.res_dict[img_size] = 1
                        else:
                            self.res_dict[img_size] += 1
        sorted(self.res_dict.items(), key=lambda x: x[1], reverse=True)

    def get_img_format(self):
        for root, dirs, files in os.walk(self.path, topdown=True):
            if files:
                for file in files:
                    file_format = file.split('.')[-1]
                    if file_format not in self.format_list:
                        print("{} is not an image !".format(file))
                        continue
                    else:
                        if file_format not in self.format_dict.keys():
                            self.format_dict[file_format] = 1
                        else:
                            self.format_dict[file_format] += 1


class ClassificationDatasetsCreate:
    def __init__(self, root_path, train_val_ratio, train_ratio,
                 train_path=None, val_path=None, test_path=None,
                 is_test=False, is_txt=True):
        self.root_path = root_path
        self.root_path_dir = os.path.dirname(root_path)
        self.train_path = train_path if train_path is not None else os.path.join(self.root_path_dir, 'train')
        os.makedirs(self.train_path) if not os.path.exists(self.train_path) else None
        self.val_path = val_path if val_path is not None else os.path.join(self.root_path_dir, 'val')
        os.makedirs(self.val_path) if not os.path.exists(self.val_path) else None
        self.is_test = is_test
        if self.is_test:
            self.test_path = test_path if test_path is not None else os.path.join(self.root_path_dir, 'test')
            os.makedirs(self.test_path) if not os.path.exists(self.test_path) else None
        self.train_val_ratio = train_val_ratio
        self.train_ratio = train_ratio

    def split_dataset(self):
        for root, dirs, files in os.walk(self.root_path, topdown=True):
            if files:
                sub_class = root.split('/')[-1]
                sub_train_dir = os.path.join(self.train_path, sub_class)
                os.makedirs(sub_train_dir) if not os.path.exists(sub_train_dir) else None
                sub_val_dir = os.path.join(self.val_path, sub_class)
                os.makedirs(sub_val_dir) if not os.path.exists(sub_val_dir) else None
                sub_test_dir = None
                if self.is_test:
                    sub_test_dir = os.path.join(self.test_path, sub_class)
                    os.makedirs(sub_test_dir) if not os.path.exists(sub_test_dir) else None
                train_val_num = int(len(files) * self.train_val_ratio)
                train_num = int(train_val_num * self.train_ratio)
                train_val_list = random.sample(os.listdir(root), train_val_num)
                train_list = random.sample(train_val_list, train_num)

                for file in files:
                    file_path = os.path.join(root, file)
                    if self.is_test:
                        if file not in train_val_list:
                            shutil.copy(file_path, sub_test_dir)
                            print("{} >>> {}".format(file, sub_test_dir))
                        elif file in train_list:
                            shutil.copy(file_path, sub_train_dir)
                            print("{} >>> {}".format(file, sub_train_dir))
                        else:
                            shutil.copy(file_path, sub_val_dir)
                            print("{} >>> {}".format(file, sub_val_dir))
                    else:
                        if file in train_list:
                            shutil.copy(file_path, sub_train_dir)
                            print("{} >>> {}".format(file, sub_train_dir))
                        else:
                            shutil.copy(file_path, sub_val_dir)
                            print("{} >>> {}".format(file, sub_val_dir))

    # def concat_dataset(self):

    # def check_no_mistakes(self):




if __name__ == '__main__':
    DIR_PATH = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/UCMerced_LandUse/UCMerced_LandUse"

    # ClassificationDatasetsStatistic Test
    # dataset_statistic = ClassificationDatasetsStatistic(dir_path=DIR_PATH)
    # dataset.get_class()
    # dataset.get_resolution()
    # dataset.get_img_format()
    # dataset_statistic.main()
    # print("\n")
    # print(dataset_statistic.class_dict)
    # print(len(dataset_statistic.class_dict.keys()))
    # print(dataset.res_set)
    # print(dataset_statistic.res_dict)
    # print(dataset_statistic.format_dict)

    # ClassificationDatasetsCreate Test
    dataset_create = ClassificationDatasetsCreate(root_path=DIR_PATH, train_val_ratio=1, train_ratio=0.8)
    dataset_create.split_dataset()
