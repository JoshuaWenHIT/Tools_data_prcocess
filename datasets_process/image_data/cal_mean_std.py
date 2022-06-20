#
#  cal_mean_std.py
#  image_data
#
#  Created by Joshua Wen on 2022/06/20.
#  Copyright © 2022 Joshua Wen. All rights reserved.
#
import numpy as np
from PIL import Image
import torchvision
from time import time
from tqdm import tqdm


def compute_mean_and_std(dataset, round_num=3):
    # 输入PyTorch的dataset，输出均值和标准差
    mean_r = 0
    mean_g = 0
    mean_b = 0
    print("计算均值>>>")
    for img_path, _ in tqdm(dataset, ncols=80):
        # print(img_path)
        img = Image.open(img_path)
        img = np.asarray(img)  # change PIL Image to numpy array
        if len(img.shape) == 3:
            mean_b += np.mean(img[:, :, 0])
            mean_g += np.mean(img[:, :, 1])
            mean_r += np.mean(img[:, :, 2])
        elif len(img.shape) == 2:
            mean_b += np.mean(img)
            mean_g += np.mean(img)
            mean_r += np.mean(img)

    mean_b /= len(dataset)
    mean_g /= len(dataset)
    mean_r /= len(dataset)

    diff_r = 0
    diff_g = 0
    diff_b = 0

    N = 0
    print("计算方差>>>")
    for img_path, _ in tqdm(dataset, ncols=80):
        img = Image.open(img_path)
        img = np.asarray(img)
        if len(img.shape) == 3:
            diff_b += np.sum(np.power(img[:, :, 0] - mean_b, 2))
            diff_g += np.sum(np.power(img[:, :, 1] - mean_g, 2))
            diff_r += np.sum(np.power(img[:, :, 2] - mean_r, 2))
            N += np.prod(img[:, :, 0].shape)
        elif len(img.shape) == 2:
            diff_b += np.sum(np.power(img - mean_b, 2))
            diff_g += np.sum(np.power(img - mean_g, 2))
            diff_r += np.sum(np.power(img - mean_r, 2))
            N += np.prod(img.shape)

    std_b = np.sqrt(diff_b / N)
    std_g = np.sqrt(diff_g / N)
    std_r = np.sqrt(diff_r / N)

    mean = (round(mean_b / 255.0, round_num),
            round(mean_g / 255.0, round_num),
            round(mean_r / 255.0, round_num))
    # mean = (mean_b.item(), mean_g.item(), mean_r.item())
    std = (round(std_b.item() / 255.0, round_num),
           round(std_g.item() / 255.0, round_num),
           round(std_r.item() / 255.0, round_num))
    return mean, std


path = "/media/joshuawen/Joshua_SSD3/Datasets/RGB/classification/UCMerced_LandUse/UCMerced_LandUse"
# train_path = path + "/train_set"
# test_path = path + "/test_set"
# val_path = path + '/val_set'

train_path = path
# test_path = path
# val_path = path

train_data = torchvision.datasets.ImageFolder(train_path)
# val_data = torchvision.datasets.ImageFolder(val_path)
# test_data = torchvision.datasets.ImageFolder(test_path)

time_start = time()

train_mean, train_std = compute_mean_and_std(train_data.imgs)
# val_mean, val_std = compute_mean_and_std(val_data.imgs)
# test_mean, test_std = compute_mean_and_std(test_data.imgs)

time_end = time()

print("计算消耗时间：", round(time_end - time_start, 4), "s")
print("训练集的平均值：{}，方差：{}".format(train_mean, train_std))
# print("验证集的平均值：{}, 方差：{}".format(val_mean, val_std))
# print("测试集的平均值：{}，方差：{}".format(test_mean, test_std))
