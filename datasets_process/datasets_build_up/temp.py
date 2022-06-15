import os

path = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/AID/AID_dataset/AID"

for root, dirs, files in os.walk(path, topdown=True):
    if root == path:
        class_dict = dict(zip(dirs, [0] * len(dirs)))
        print(class_dict)
    print("#" * 20)
    print(root)
    print("#" * 20)
    print(dirs)
    print("#" * 20)
    print(files)
