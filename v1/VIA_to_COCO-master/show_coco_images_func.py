#
#  show_coco_images_func.py
#  Display the COCO type annotation results on the original images.
#
#  Created by JoshuaWen on 2022/06/04.
#  Copyright © 2022 JoshuaWen. All rights reserved.
#
import time
from pycocotools.coco import COCO
import pylab
import cv2
import os
import numpy as np
import mmcv
import gc


def add_annotation_on_original_image(coco, imgId, img_path, result_path):
    img_dict = coco.loadImgs(imgId)[0]
    image_name = img_dict['file_name']
    print(image_name)
    img = mmcv.imread(os.path.join(img_path, image_name))
    annIds = coco.getAnnIds(imgIds=img_dict['id'], catIds=[], iscrowd=None)
    # print(annIds)
    anns = coco.loadAnns(annIds)
    showonce = True
    for ann in anns:
        if type(ann['segmentation']) == list and showonce:
            print(ann['segmentation'])
            showonce = False
        if type(ann['segmentation']) != list:
            print(ann['segmentation'])
        mask = coco.annToMask(ann).astype(np.bool_)
        color_mask = np.random.randint(0, 256, (1, 3), dtype=np.uint8)
        # print(mask.shape)
        # print(img.shape)
        img[mask] = img[mask] * 0.5 + color_mask * 0.5  # 在图片上修改像素值，画出掩码
        # cv2.imshow('mask_image', img)#显示
        # cv2.waitKey(10) #必须有，不然上一句的显示不起效果。
    for j in range(len(anns)):
        coordinate = []
        coordinate.append(anns[j]['bbox'][0])
        coordinate.append(anns[j]['bbox'][1] + anns[j]['bbox'][3])
        coordinate.append(anns[j]['bbox'][0] + anns[j]['bbox'][2])
        coordinate.append(anns[j]['bbox'][1])
        # print(coordinate)
        left = np.rint(coordinate[0])
        right = np.rint(coordinate[1])
        top = np.rint(coordinate[2])
        bottom = np.rint(coordinate[3])
        # 左上角坐标, 右下角坐标
        cv2.rectangle(img,
                      (int(left), int(right)),
                      (int(top), int(bottom)),
                      (0, 255, 0),
                      2)
        cv2.putText(img,
                    str(anns[j]['category_id']),
                    (int(left), int(right)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2
                    )
    cv2.imshow('result_image', img)  # 显示
    cv2.imwrite(os.path.join(result_path, image_name), img=img)
    # if (i + 1) % 5000 == 0:
    #     time.sleep(10)
    #     del img
    #     gc.collect()
    cv2.waitKey(10)  # 必须有，不然上一句的显示不起效果。


def get_coco_annotation(ann_path):
    coco = COCO(ann_path)
    cats = coco.loadCats(coco.getCatIds())
    catNms = [cat['name'] for cat in cats]
    print('COCO categories: \n{}\n'.format(' '.join(catNms)))
    supNms = set([cat['supercategory'] for cat in cats])
    print('COCO supercategories: \n{}'.format(' '.join(supNms)))
    catIds = coco.getCatIds(catNms=catNms, supNms=supNms)
    print(catIds)
    imgIds= coco.getImgIds()
    print(imgIds)
    print(len(imgIds))
    return coco, imgIds


if __name__ == '__main__':
    pylab.rcParams['figure.figsize'] = (8.0, 10.0)
    img_path = '/home/joshuawen/data/coco/images/val2014/'
    annFile = '/home/joshuawen/data/coco/annotations/annotations/instances_val2014.json'
    result_path = '/home/joshuawen/data/coco/images/res'

    coco, imgIds = get_coco_annotation(ann_path=annFile)
    for i in range(len(imgIds)):
        add_annotation_on_original_image(coco, imgIds[i], img_path, result_path)
    print("Finished !")


