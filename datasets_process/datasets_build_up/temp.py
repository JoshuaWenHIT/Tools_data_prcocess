import os
from custom_creator import CustomDataset

path = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/NWPU VHR-10 dataset"

# for root, dirs, files in os.walk(path, topdown=True):
#     if root == path:
#         class_dict = dict(zip(dirs, [0] * len(dirs)))
#         print(class_dict)
#     print("#" * 20)
#     print(root)
#     print("#" * 20)
#     print(dirs)
#     print("#" * 20)
#     print(files)

custom_dataset = CustomDataset(root_path=path)
custom_dataset.get_path(img_flag_str='image set', ann_flag_str='ground')
custom_dataset.get_image_format()
custom_dataset.get_image_resolution()
custom_dataset.get_annotation_format()
print(custom_dataset.img_fm)
print(custom_dataset.img_res)
print(custom_dataset.ann_fm)
