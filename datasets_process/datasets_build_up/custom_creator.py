#
#  custom_creator.py
#  datasets_build_up
#
#  Created by Joshua Wen on 2022/06/27.
#  Copyright © 2022 Joshua Wen. All rights reserved.
#
import os
import shutil
import random
from PIL import Image


class CustomDataset:
    def __init__(self, root_path, *args, **kwargs):
        self.root_path = root_path
        self.img_root_path = []
        self.ann_root_path = []

        self.img_fm = {}
        self.img_res = {}
        self.ann_fm = {}

        self.class_dict = kwargs

        self.__dir_tuple = args
        self.__format_list = ['png', 'jpg', 'jpeg', 'tif', 'tiff', 'bmp']

    def get_path(self, img_flag_str='', ann_flag_str=''):
        for item in os.listdir(self.root_path):
            if os.path.isdir(os.path.join(self.root_path, item)) and img_flag_str in item:
                self.img_root_path.append(os.path.join(self.root_path, item))
            if os.path.isdir(os.path.join(self.root_path, item)) and ann_flag_str in item:
                self.ann_root_path.append(os.path.join(self.root_path, item))
        return self.img_root_path, self.ann_root_path

    def get_image_format(self):
        for img_root_path in self.img_root_path:
            for item in os.listdir(img_root_path):
                item_fm = item.split('.')[-1]
                if item_fm not in self.__format_list:
                    print("ERROR: {} is not an image!".format(os.path.join(img_root_path, item)))
                    continue
                else:
                    if item_fm not in self.img_fm.keys():
                        self.img_fm[item_fm] = 1
                    else:
                        self.img_fm[item_fm] += 1
        return self.img_fm

    def get_image_resolution(self):
        for img_root_path in self.img_root_path:
            for item in os.listdir(img_root_path):
                item_fm = item.split('.')[-1]
                if item_fm not in self.__format_list:
                    print("ERROR: {} is not an image!".format(os.path.join(img_root_path, item)))
                    continue
                else:
                    print("\rresolution calculate: {}   ".format(item), end='')
                    img_size = Image.open(os.path.join(img_root_path, item)).size
                    if img_size not in self.img_res.keys():
                        self.img_res[img_size] = 1
                    else:
                        self.img_res[img_size] += 1
        sorted(self.img_res.items(), key=lambda x: x[1], reverse=True)
        return self.img_res

    def get_annotation_format(self):
        for ann_root_path in self.ann_root_path:
            for item in os.listdir(ann_root_path):
                item_fm = item.split('.')[-1]
                if item_fm not in self.ann_fm.keys():
                    self.ann_fm[item_fm] = 1
                else:
                    self.ann_fm[item_fm] += 1
        return self.ann_fm


class CustomDatasetCreator:
    def __init__(self, dataset, train_val_ratio, train_ratio, is_test=False):
        self.dataset = dataset

        self.train_root_path = os.path.join(self.dataset.root_path, 'train')
        self.val_root_path = os.path.join(self.dataset.root_path, 'val')
        self.test_root_path = os.path.join(self.dataset.root_path, 'test')
        self.train_ann_path = os.path.join(self.train_root_path, 'ann')
        self.val_ann_path = os.path.join(self.val_root_path, 'ann')
        self.test_ann_path = os.path.join(self.test_root_path, 'ann')
        self.train_img_path = os.path.join(self.train_root_path, 'img')
        self.val_img_path = os.path.join(self.val_root_path, 'img')
        self.test_img_path = os.path.join(self.test_root_path, 'img')
        os.makedirs(self.train_ann_path, exist_ok=True)
        os.makedirs(self.val_ann_path, exist_ok=True)
        if is_test:
            os.makedirs(self.test_ann_path, exist_ok=True)

        self.train_val_ratio = train_val_ratio
        self.train_ratio = train_ratio
        self.is_test = is_test

    def split(self):
        """
        Note:
            1. Currently, only for datasets with independent labels
            2. MAKE SURE that there are no annotation files which have the same file name.
        """

        os.makedirs(self.train_root_path, exist_ok=True)
        os.makedirs(self.val_root_path, exist_ok=True)
        if self.is_test:
            os.makedirs(self.test_root_path, exist_ok=True)
        for ann_root_path in self.dataset.ann_root_path:
            train_val_num = int(len(os.listdir(ann_root_path)) * self.train_val_ratio)
            train_num = int(train_val_num * self.train_ratio)
            train_val_list = random.sample(os.listdir(ann_root_path), train_val_num)
            train_list = random.sample(train_val_list, train_num)
            for item in os.listdir(ann_root_path):
                item_path = os.path.join(ann_root_path, item)
                if self.is_test:
                    if item not in train_val_list:
                        shutil.copy(item_path, self.test_root_path)
                        print("{} >>> {}".format(item, self.test_root_path))
                    elif item in train_list:
                        shutil.copy(item_path, self.train_root_path)
                        print("{} >>> {}".format(item, self.train_root_path))
                    else:
                        shutil.copy(item_path, self.val_root_path)
                        print("{} >>> {}".format(item, self.val_root_path))
                else:
                    if item in train_list:
                        shutil.copy(item_path, self.train_root_path)
                        print("{} >>> {}".format(item, self.train_root_path))
                    else:
                        shutil.copy(item_path, self.val_root_path)
                        print("{} >>> {}".format(item, self.val_root_path))
        os.makedirs(os.path.join(self.train_root_path, 'images'), exist_ok=True)
        os.makedirs(os.path.join(self.val_root_path, 'images'), exist_ok=True)
        for file in os.listdir(os.path.join(self.train_path, 'xml')):
            file_path = os.path.join(self.root_path_dir, 'images', file.replace('.xml', '.jpg'))
            shutil.copy(file_path, os.path.join(self.train_path, 'images'))
            print("{} >>> {}".format(file.replace('.xml', '.jpg'), os.path.join(self.train_path, 'images')))
        for file in os.listdir(os.path.join(self.val_path, 'xml')):
            file_path = os.path.join(self.root_path_dir, 'images', file.replace('.xml', '.jpg'))
            shutil.copy(file_path, os.path.join(self.val_path, 'images'))
            print("{} >>> {}".format(file.replace('.xml', '.jpg'), os.path.join(self.val_path, 'images')))
        if self.is_test:
            os.makedirs(os.path.join(self.test_root_path, 'images'), exist_ok=True)
            for file in os.listdir(os.path.join(self.test_path, 'xml')):
                file_path = os.path.join(self.root_path_dir, 'images', file.replace('.xml', '.jpg'))
                shutil.copy(file_path, os.path.join(self.test_path, 'images'))
                print("{} >>> {}".format(file.replace('.xml', '.jpg'), os.path.join(self.test_path, 'images')))

    def txt_to_xml(self):
        pass

