import json
import os.path
from collections import defaultdict
from tqdm import tqdm


def read_json(file_path: object, flag: object = 'print') -> object:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if flag == 'print':
        if isinstance(data, list):
            for key, value in data[0].items():
                # print(f'{key}: {value}')
                print(f'{key}')
            # print(data['categories'])
        elif isinstance(data, dict):
            for key, value in data.items():
                # print(f'{key}: {value}')
                print(f'{key}')
            # print(data['categories'])

    return data, type(data)


if __name__ == '__main__':
    file_path = "/home/HDD/Temp/predictions.json"
    data, data_type = read_json(file_path, flag='print')

    images_list = []
    for pred in data:
        image_id = pred['image_id']
        if image_id not in images_list:
            images_list.append(image_id)
    print(len(images_list))

    ann_path = "/home/HDD/Datasets/SAR/SARDet-100K/annotations/val.json"
    ann, ann_type = read_json(ann_path, flag='print')
    # print(ann['images'])
    # print(ann['categories'])
