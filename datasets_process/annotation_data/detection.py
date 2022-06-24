import sys
from PIL import Image
import os
import numpy as np
from datasets_process.datasets_build_up.detection import DetectionDatasetsStatistic

if sys.version_info[0] == 2:
    import xml.etree.cElementTree as ET
else:
    import xml.etree.ElementTree as ET


class DetectionAnnotationTools:
    def __init__(self, root_path, class_dict):
        self.root_path = root_path
        self.img_root_path = os.path.join(self.root_path, 'images')
        self.ann_root_path = os.path.join(self.root_path, 'annotations')
        self.class_dict = class_dict

    def annotation_check(self, img_type='.jpg', ann_type='.xml'):
        i = 0
        for root, dirs, files in os.walk(self.ann_root_path, topdown=True):
            if files and ann_type == '.xml':
                for file in files:
                    i += 1
                    img_size = Image.open(os.path.join(self.img_root_path, file.split('.')[0] + img_type)).size
                    target = ET.parse(os.path.join(root, file)).getroot()
                    res = []
                    print(file)
                    for obj in target.iter('object'):
                        # difficult = int(obj.find('difficult').text) == 1
                        #
                        # if not keep_difficult and difficult:
                        #     continue
                        name = obj.find('name').text.lower().strip()
                        bbox = obj.find('bndbox')
                        pts = ['xmin', 'ymin', 'xmax', 'ymax']
                        bndbox = []
                        for i, pt in enumerate(pts):
                            cur_pt = int(bbox.find(pt).text) - 1
                            # scale height or width
                            cur_pt = float(cur_pt) / img_size[1] if i % 2 == 0 else float(cur_pt) / img_size[0]

                            bndbox.append(cur_pt)
                        print(name)
                        label_idx = dict(zip(self.class_dict.keys(), range(len(self.class_dict.keys()))))[name]
                        bndbox.append(label_idx)
                        res += [bndbox]  # [xmin, ymin, xmax, ymax, label_ind]
                        # img_id = target.find('filename').text[:-4]
                    print(res)
                    if np.array(res)[:, :4].any() < 0:
                        print("\nERROR !\n")
                        exit(0)

    def change_all_xml(self):
        filelist = os.listdir(self.ann_root_path)
        # 打开xml文档
        for xmlfile in filelist:
            print(xmlfile)
            doc = ET.parse(os.path.join(self.ann_root_path, xmlfile))
            root = doc.getroot()
            sub1 = root.find('filename')  # 找到filename标签，
            sub1.text = os.path.splitext(xmlfile)[0] + '.jpg'  # 修改标签内容
            sub2 = root.find('folder')
            sub2.text = self.root_path.split('/')[-1]
            sub3 = root.find('path')
            sub3.text = os.path.join(self.img_root_path, os.path.splitext(xmlfile)[0] + '.jpg')

            doc.write(os.path.join(self.ann_root_path, xmlfile))  # 保存修改
            print('{} is changed !'.format(xmlfile))


if __name__ == '__main__':
    DIR_PATH = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/RSD-6"

    dataset_statistic = DetectionDatasetsStatistic(dir_path=os.path.join(DIR_PATH, DIR_PATH.split('/')[-1]))
    dataset_statistic.get_class()
    print(dataset_statistic.class_dict.keys())

    ann_tools = DetectionAnnotationTools(root_path=DIR_PATH, class_dict=dataset_statistic.class_dict)
    # ann_tools.annotation_check()
    ann_tools.change_all_xml()
