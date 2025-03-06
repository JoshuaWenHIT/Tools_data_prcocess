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
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
import json
from collections import OrderedDict


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
                    print("\rresolution calculating: {}   ".format(item), end='')
                    img_size = Image.open(os.path.join(img_root_path, item)).size
                    if img_size not in self.img_res.keys():
                        self.img_res[img_size] = 1
                    else:
                        self.img_res[img_size] += 1
        sorted(self.img_res.items(), key=lambda x: x[1], reverse=True)
        print("\n")
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
        os.makedirs(self.train_img_path, exist_ok=True)
        os.makedirs(self.val_img_path, exist_ok=True)
        if is_test:
            os.makedirs(self.test_ann_path, exist_ok=True)
            os.makedirs(self.test_img_path, exist_ok=True)

        self.train_val_ratio = train_val_ratio
        self.train_ratio = train_ratio
        self.is_test = is_test

    def split(self):
        """
        Note:
            1. Currently, only for datasets with independent labels
            2. MAKE SURE that there are no annotation files which have the same file name.
        """
        # for ann_root_path in self.dataset.ann_root_path:
        train_val_num = int(len(os.listdir(self.dataset.ann_root_path[0])) * self.train_val_ratio)
        train_num = int(train_val_num * self.train_ratio)
        train_val_list = random.sample(os.listdir(self.dataset.ann_root_path[0]), train_val_num)
        train_list = random.sample(train_val_list, train_num)
        for item in os.listdir(self.dataset.ann_root_path[0]):
            item_path = os.path.join(self.dataset.ann_root_path[0], item)
            if self.is_test:
                if item not in train_val_list:
                    shutil.copy(item_path, self.test_ann_path)
                    print("{} >>> {}".format(item, self.test_ann_path))
                elif item in train_list:
                    shutil.copy(item_path, self.train_ann_path)
                    print("{} >>> {}".format(item, self.train_ann_path))
                else:
                    shutil.copy(item_path, self.val_ann_path)
                    print("{} >>> {}".format(item, self.val_ann_path))
            else:
                if item in train_list:
                    shutil.copy(item_path, self.train_ann_path)
                    print("{} >>> {}".format(item, self.train_ann_path))
                else:
                    shutil.copy(item_path, self.val_ann_path)
                    print("{} >>> {}".format(item, self.val_ann_path))

        img_fm = '.' + list(self.dataset.img_fm.keys())[0]
        ann_fm = '.' + list(self.dataset.ann_fm.keys())[0]
        # for img_root_path in self.dataset.img_root_path:
        for item in os.listdir(self.train_ann_path):
            item_path = os.path.join(self.dataset.img_root_path[1], item.replace(ann_fm, img_fm))
            shutil.copy(item_path, self.train_img_path)
            print("{} >>> {}".format(item.replace(ann_fm, img_fm), self.train_img_path))
        for item in os.listdir(self.val_ann_path):
            item_path = os.path.join(self.dataset.img_root_path[1], item.replace(ann_fm, img_fm))
            shutil.copy(item_path, self.val_img_path)
            print("{} >>> {}".format(item.replace(ann_fm, img_fm), self.val_img_path))
        if self.is_test:
            for item in os.listdir(self.test_ann_path):
                item_path = os.path.join(self.dataset.img_root_path[1], item.replace(ann_fm, img_fm))
                shutil.copy(item_path, self.test_img_path)
                print("{} >>> {}".format(item.replace(ann_fm, img_fm), self.test_img_path))

    def concat(self):
        # TODO: concat different datasets into one dataset.
        pass


class XmlCreator:
    def __init__(self, dataset, dataset_creator, is_test=False):
        self.dataset = dataset
        self.dataset_creator = dataset_creator

        self.train_xml_path = os.path.join(dataset_creator.train_root_path, 'xml')
        self.val_xml_path = os.path.join(dataset_creator.val_root_path, 'xml')
        os.makedirs(self.train_xml_path, exist_ok=True)
        os.makedirs(self.val_xml_path, exist_ok=True)
        if is_test:
            self.test_xml_path = os.path.join(dataset_creator.test_root_path, 'xml')
            os.makedirs(self.test_xml_path, exist_ok=True)

    def main(self):
        count = 0
        img_fm = '.' + list(self.dataset.img_fm.keys())[0]
        ann_fm = '.' + list(self.dataset.ann_fm.keys())[0]
        for item in os.listdir(self.dataset_creator.train_img_path):
            list_top = []
            list_bbox = []
            img_path = os.path.join(self.dataset_creator.train_img_path, item)
            txt_path = os.path.join(self.dataset_creator.train_ann_path, item.replace(img_fm, ann_fm))
            xml_path = os.path.join(self.train_xml_path, item.replace(img_fm, '.xml'))

            img = Image.open(img_path)
            img_w = img.size[0]
            img_h = img.size[1]
            img_d = len(img.split())
            width = str(img_w)
            height = str(img_h)
            depth = str(img_d)
            occlusion = '0'
            pose = 'unknown'
            truncated = '0'
            difficult = '0'
            list_top.extend([xml_path, self.dataset_creator.train_img_path, item, width, height, depth])

            for line in open(txt_path, 'r'):
                line = line.strip()
                if not line.split():
                    continue
                info = line.split(',')
                xmin = int(info[0].strip('(').strip(' '))
                ymin = int(info[1].strip(')').strip(' '))
                xmax = int(info[2].strip('(').strip(' '))
                ymax = int(info[3].strip(')').strip(' '))
                name = self.dataset.class_dict[info[4].strip(' ')]
                list_bbox.extend([name, str(xmin), str(ymin), str(xmax), str(ymax),
                                  pose, truncated, difficult, occlusion])
            self.txt_to_xml(list_top, list_bbox)
            count += 1
            print(count, xml_path)

    def __indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.__indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    @staticmethod
    def _add_bbox(annotation_root, list_bndbox):
        for i in range(0, len(list_bndbox), 9):
            object_element = ET.Element('object')
            name_element = SubElement(object_element, 'name')
            name_element.text = list_bndbox[i]

            bndbox_element = SubElement(object_element, 'bndbox')
            xmin_element = SubElement(bndbox_element, 'xmin')
            xmin_element.text = str(list_bndbox[i + 1])

            ymin_element = SubElement(bndbox_element, 'ymin')
            ymin_element.text = str(list_bndbox[i + 2])

            xmax_element = SubElement(bndbox_element, 'xmax')
            xmax_element.text = str(list_bndbox[i + 3])

            ymax_element = SubElement(bndbox_element, 'ymax')
            ymax_element.text = str(list_bndbox[i + 4])

            pose_element = SubElement(object_element, 'pose')
            pose_element.text = list_bndbox[i + 5]

            truncated_element = SubElement(object_element, 'truncated')
            truncated_element.text = list_bndbox[i + 6]

            difficult_element = SubElement(object_element, 'difficult')
            difficult_element.text = list_bndbox[i + 7]

            flag_element = SubElement(object_element, 'occlusion')
            flag_element.text = list_bndbox[i + 8]

            annotation_root.append(object_element)

        return annotation_root

    def _add_image_info(self, list_top):
        annotation_root = ET.Element('annotation')
        # annotation_root.set('verified', 'no')
        tree = ET.ElementTree(annotation_root)
        # '''
        # 0:xml_savepath 1:folder,2:filename,3:path
        # 4:checked,5:width,6:height,7:depth
        # '''
        folder_element = ET.Element('folder')
        folder_element.text = list_top[1]
        annotation_root.append(folder_element)

        filename_element = ET.Element('filename')
        filename_element.text = list_top[2]
        annotation_root.append(filename_element)

        source_element = ET.Element('source')
        database_element = SubElement(source_element, 'database')
        database_element.text = self.dataset.root_path.split('/')[-1]
        annotation_root.append(source_element)

        size_element = ET.Element('size')
        width_element = SubElement(size_element, 'width')
        width_element.text = str(list_top[3])
        height_element = SubElement(size_element, 'height')
        height_element.text = str(list_top[4])
        depth_element = SubElement(size_element, 'depth')
        depth_element.text = str(list_top[5])
        annotation_root.append(size_element)

        segmented_person_element = ET.Element('segmented')
        segmented_person_element.text = '0'
        annotation_root.append(segmented_person_element)

        return tree, annotation_root

    def txt_to_xml(self, list_top, list_bbox):
        tree, annotation_root = self._add_image_info(list_top)
        annotation_root = self._add_bbox(annotation_root, list_bbox)
        self.__indent(annotation_root)
        tree.write(list_top[0], encoding='utf-8', xml_declaration=True)


class XmlToJson:
    def __init__(self, class_dict):
        self.class_dict = class_dict

        self.coco = OrderedDict()
        self.coco['images'] = []
        self.coco['type'] = 'instances'
        self.coco['annotations'] = []
        self.coco['categories'] = []

        self.category_set = OrderedDict()
        self.image_set = OrderedDict()

        # category_item_id = 0
        self.image_id = 000000
        self.annotation_id = 0

    def xml_to_json(self, xml_path, json_file_path):
        xml_list = os.listdir(xml_path)
        xml_list.sort(key=lambda x: x.split('.')[0])
        for f in xml_list:
            if not f.endswith('.xml'):
                continue

            bndbox = dict()
            size = dict()
            current_image_id = None
            current_category_id = None
            file_name = None
            size['width'] = None
            size['height'] = None
            size['depth'] = None

            xml_file = os.path.join(xml_path, f)
            print(xml_file)

            tree = ET.parse(xml_file)
            root = tree.getroot()
            if root.tag != 'annotation':
                raise Exception('pascal voc xml root element should be annotation, rather than {}'.format(root.tag))

            # elem is <folder>, <filename>, <size>, <object>
            for elem in root:
                current_parent = elem.tag
                current_sub = None
                object_name = None

                if elem.tag == 'folder':
                    continue

                if elem.tag == 'filename':
                    file_name = elem.text
                    if file_name in self.category_set:
                        raise Exception('file_name duplicated')

                # add img item only after parse <size> tag
                elif current_image_id is None and file_name is not None and size['width'] is not None:
                    if file_name not in self.image_set:
                        current_image_id = self.add_img_item(file_name, size)
                        print('add image with {} and {}'.format(file_name, size))
                    else:
                        raise Exception('duplicated image: {}'.format(file_name))
                        # subelem is <width>, <height>, <depth>, <name>, <bndbox>
                for subelem in elem:
                    bndbox['xmin'] = None
                    bndbox['xmax'] = None
                    bndbox['ymin'] = None
                    bndbox['ymax'] = None

                    current_sub = subelem.tag
                    if current_parent == 'object' and subelem.tag == 'name':
                        object_name = subelem.text
                        if object_name == 'w':
                            raise Exception('%s.' % f)
                        if object_name not in self.category_set:
                            current_category_id = self.add_cat_item(object_name)
                        else:
                            current_category_id = self.category_set[object_name]

                    elif current_parent == 'size':
                        if size[subelem.tag] is not None:
                            raise Exception('xml structure broken at size tag.')
                        size[subelem.tag] = int(subelem.text)

                    # option is <xmin>, <ymin>, <xmax>, <ymax>, when subelem is <bndbox>
                    for option in subelem:
                        if current_sub == 'bndbox':
                            if bndbox[option.tag] is not None:
                                raise Exception('xml structure corrupted at bndbox tag.')
                            bndbox[option.tag] = int(option.text)

                    # only after parse the <object> tag
                    if bndbox['xmin'] is not None:
                        if object_name is None:
                            raise Exception('xml structure broken at bndbox tag')
                        if current_image_id is None:
                            raise Exception('xml structure broken at bndbox tag')
                        if current_category_id is None:
                            raise Exception('xml structure broken at bndbox tag')
                        bbox = [bndbox['xmin'], bndbox['ymin'], bndbox['xmax'] - bndbox['xmin'],
                                bndbox['ymax'] - bndbox['ymin']]
                        print('add annotation with {},{},{},{}'
                              .format(object_name, current_image_id, current_category_id, bbox))
                        self.add_ann_item(object_name, current_image_id, current_category_id, bbox)

        json_dict = json.dumps(self.coco)
        print(json_dict)
        with open(json_file_path, 'w') as j:
            j.write(json_dict)

    def add_cat_item(self, name):
        category_item = dict()
        category_item['supercategory'] = 'none'
        # self.category_item_id += 1
        # category_item['id'] = category_item_id
        # category_item['name'] = name
        # self.coco['categories'].append(category_item)
        # self.category_set[name] = category_item_id
        for k, v in self.class_dict.items():
            if name == v:
                category_item['id'] = int(k)
                category_item['name'] = name
                self.coco['categories'].append(category_item)
                self.category_set[name] = int(k)
        return category_item['id']

    def add_img_item(self, file_name, size):
        if file_name is None:
            raise Exception('Could not find filename tag in xml file.')
        if size['width'] is None:
            raise Exception('Could not find width tag in xml file.')
        if size['height'] is None:
            raise Exception('Could not find height tag in xml file.')
        self.image_id += 1
        image_item = dict()
        image_item['id'] = self.image_id
        image_item['file_name'] = file_name
        image_item['width'] = size['width']
        image_item['height'] = size['height']
        self.coco['images'].append(image_item)
        self.image_set.get(file_name)
        return self.image_id

    def add_ann_item(self, object_name, image_id, category_id, bbox):
        annotation_item = dict()
        annotation_item['segmentation'] = []
        seg = [bbox[0], bbox[1], bbox[0], bbox[1] + bbox[3], bbox[0] + bbox[2], bbox[1] + bbox[3], bbox[0] + bbox[2],
               bbox[1]]
        annotation_item['segmentation'].append(seg)
        annotation_item['area'] = bbox[2] * bbox[3]
        annotation_item['iscrowd'] = 0
        annotation_item['ignore'] = 0
        annotation_item['image_id'] = image_id
        annotation_item['bbox'] = bbox
        annotation_item['category_id'] = category_id
        self.annotation_id += 1
        annotation_item['id'] = self.annotation_id
        self.coco['annotations'].append(annotation_item)
