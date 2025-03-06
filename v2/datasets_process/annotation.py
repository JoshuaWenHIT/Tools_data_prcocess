import json
import os.path
from collections import defaultdict
from tqdm import tqdm


def read_json(file_path: object, flag: object = 'print') -> object:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if flag == 'print':
        for key, value in data.items():
            # print(f'{key}: {value}')
            print(f'{key}')
        print(data['categories'])

    return data


def coco_json_sat(file_path, flag=None):
    data = read_json(file_path, flag=flag)

    category_id_to_name = {category['id']: category['name'] for category in data['categories']}
    category_instance_count = defaultdict(int)

    for annotation in data['annotations']:
        category_id = annotation['category_id']
        category_instance_count[category_id] += 1

    for category_id, instance_count in category_instance_count.items():
        category_name = category_id_to_name.get(category_id, "Unknown")
        print(f"Category '{category_name}' (ID: {category_id}): {instance_count} instances")

    return category_instance_count


def bbox_convert(img_w, img_h, bbox):
    dw = 1. / img_w
    dh = 1. / img_h
    x = bbox[0] + bbox[2] / 2.0
    y = bbox[1] + bbox[3] / 2.0
    w = bbox[2]
    h = bbox[3]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def coco_json_to_yolo_txt(src_path, save_path, flag=None):
    data = read_json(src_path, flag=flag)
    # category_id_to_name = {category['id']: category['name'] for category in data['categories']}

    # if save_path is None:
    #     yolo_txt_path = src_path.replace('.json', '.txt')
    # else:
    #     yolo_txt_path = save_path

    for i in tqdm(range(len(data['images']))):
        img_name = data['images'][i]['file_name']
        img_width = data['images'][i]['width']
        img_height = data['images'][i]['height']
        img_id = data['images'][i]['id']

        yolo_txt_name = img_name.split('.')[0] + '.txt'
        yolo_txt_file = open(os.path.join(save_path, yolo_txt_name), 'w')

        for ann in data['annotations']:
            if ann['image_id'] == img_id:
                yolo_bbox = bbox_convert(img_width, img_height, ann['bbox'])
                yolo_txt_file.write(
                    '{} {} {} {} {}\n'.format(ann['category_id'],
                                              yolo_bbox[0],
                                              yolo_bbox[1],
                                              yolo_bbox[2],
                                              yolo_bbox[3])
                )
        yolo_txt_file.close()



if __name__ == '__main__':
    file_path = '/home/HDD/Datasets/SAR/SARDet-100K/annotations/val.json'
    save_path = '/home/HDD/Datasets/SAR/SARDet-100K/labels/val'
    # read_json(file_path, flag='print')
    # cl_count = coco_json_sat(file_path)
    coco_json_to_yolo_txt(file_path, save_path)
