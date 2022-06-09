#
#  classification.py
#  data_analysis
#
#  Created by Joshua Wen on 2022/06/08.
#  Copyright © 2022 Joshua Wen. All rights reserved.
#
import os
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


if __name__ == '__main__':
    DIR_PATH = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/RSI-CB256/other objects"
    dataset_statistic = ClassificationDatasetsStatistic(dir_path=DIR_PATH)
    # dataset.get_class()
    # dataset.get_resolution()
    # dataset.get_img_format()
    dataset_statistic.main()
    print("\n")
    print(dataset_statistic.class_dict)
    print(len(dataset_statistic.class_dict.keys()))
    # print(dataset.res_set)
    print(dataset_statistic.res_dict)
    print(dataset_statistic.format_dict)

