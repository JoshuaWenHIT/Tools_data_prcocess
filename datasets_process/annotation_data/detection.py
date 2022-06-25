import sys
from PIL import Image
import cv2
import os
import numpy as np
from datasets_process.datasets_build_up.detection import DetectionDatasetsStatistic

if sys.version_info[0] == 2:
    import xml.etree.cElementTree as ET
else:
    import xml.etree.ElementTree as ET
import xml.dom.minidom


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
                        if name == 'w':
                            raise Exception('error name')
                        label_idx = dict(zip(self.class_dict.keys(), range(len(self.class_dict.keys()))))[name]
                        bndbox.append(label_idx)
                        res += [bndbox]  # [xmin, ymin, xmax, ymax, label_ind]
                        # img_id = target.find('filename').text[:-4]
                    print(res)
                    if np.array(res)[:, :4].any() < 0:
                        print("\nERROR !\n")
                        exit(0)
                print(i)

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

    def draw_anchor(self, save_path=None):
        if not save_path:
            save_path = self.img_root_path.replace('images', 'res')
        os.makedirs(save_path, exist_ok=True)
        imagelist = os.listdir(self.img_root_path)
        for image in imagelist:
            image_pre, ext = os.path.splitext(image)
            imgfile = os.path.join(self.img_root_path, image)
            xmlfile = os.path.join(self.ann_root_path, image_pre + '.xml')
            DOMTree = xml.dom.minidom.parse(xmlfile)
            collection = DOMTree.documentElement
            img = cv2.imread(imgfile)
            filenamelist = collection.getElementsByTagName("filename")
            filename = filenamelist[0].childNodes[0].data
            print(filename)
            objectlist = collection.getElementsByTagName("object")
            for objects in objectlist:
                namelist = objects.getElementsByTagName('name')
                objectname = namelist[0].childNodes[0].data
                bndbox = objects.getElementsByTagName('bndbox')
                for box in bndbox:
                    x1_list = box.getElementsByTagName('xmin')
                    x1 = int(x1_list[0].childNodes[0].data)
                    y1_list = box.getElementsByTagName('ymin')
                    y1 = int(y1_list[0].childNodes[0].data)
                    x2_list = box.getElementsByTagName('xmax')  # 注意坐标，看是否需要转换
                    x2 = int(x2_list[0].childNodes[0].data)
                    y2_list = box.getElementsByTagName('ymax')
                    y2 = int(y2_list[0].childNodes[0].data)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
                    cv2.putText(img, objectname, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), thickness=2)
                    print(os.path.join(save_path, filename))
                    cv2.imwrite(os.path.join(save_path, filename), img)  # save picture


if __name__ == '__main__':
    DIR_PATH = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/RSD-6"

    dataset_statistic = DetectionDatasetsStatistic(dir_path=os.path.join(DIR_PATH, DIR_PATH.split('/')[-1]))
    dataset_statistic.get_class()
    print(dataset_statistic.class_dict.keys())

    ann_tools = DetectionAnnotationTools(root_path=DIR_PATH, class_dict=dataset_statistic.class_dict)
    ann_tools.annotation_check()
    # ann_tools.change_all_xml()
