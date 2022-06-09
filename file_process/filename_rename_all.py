import os
from pathlib import Path


def rename(dir_path, store_path, name_paradigm):
    if name_paradigm == "number":
        name = 1
        for file in os.listdir(dir_path):
            file_path = Path(os.path.join(dir_path, file))
            new_file_path = os.path.join(store_path, str(name) + file_path.suffix)
            print(new_file_path)
            os.rename(file_path, new_file_path)
            name += 1


if __name__ == '__main__':
    dir_path = "/media/joshuawen/JoshuaWen/Joshua/Data/exp/CenterNet_v2/video_orig/2"
    store_path = "/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_original/2"
    name_paradigm = ["number", "letter", "others"]
    rename(dir_path=dir_path, store_path=store_path, name_paradigm=name_paradigm[0])
