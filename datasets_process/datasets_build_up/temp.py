import os
from custom_creator import CustomDataset, CustomDatasetCreator, XmlCreator, XmlToJson

path = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/NWPU_VHR-10"
class_dict = {"1": "airplane", "2": "ship", "3": "storage tank", "4": "baseball diamond", "5": "tennis court",
              "6": "basketball court", "7": "ground track field", "8": "harbor", "9": "bridge", "10": "vehicle"}

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

# custom_dataset = CustomDataset(root_path=path, **class_dict)
# custom_dataset.get_path(img_flag_str='image set', ann_flag_str='ground')
# custom_dataset.get_image_format()
# custom_dataset.get_image_resolution()
# custom_dataset.get_annotation_format()
# print(custom_dataset.img_fm)
# print(custom_dataset.img_res)
# print(custom_dataset.ann_fm)
# print(custom_dataset.img_root_path)

# custom_dataset_creator = CustomDatasetCreator(custom_dataset, train_val_ratio=1.0, train_ratio=0.9)
# custom_dataset_creator.split()
# xml_creator = XmlCreator(custom_dataset, custom_dataset_creator)
# xml_creator.main()

XmlToJson(class_dict).xml_to_json(xml_path="/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/NWPU_VHR-10/train/xml",
                                  json_file_path="/media/joshuawen/Joshua_SSD3/Datasets/RGB/detection/NWPU_VHR-10/train/nwpu_vhr-10_train.json")