import cv2
import numpy as np
from PIL import Image
from pyheatmap.heatmap import HeatMap


def apply_heatmap(image, data):
    """image是原图，data是坐标"""
    '''创建一个新的与原图大小一致的图像，color为0背景为黑色。这里这样做是因为在绘制热力图的时候如果不选择背景图，画出来的图与原图大小不一致（根据点的坐标来的），导致无法对热力图和原图进行加权叠加，因此，这里我新建了一张背景图。'''
    image1 = cv2.imread(image)
    print(image1.shape)
    # image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2RGB)
    background = Image.new("RGB", (image1.shape[1], image1.shape[0]), color=0)
    # 开始绘制热度图
    hm = HeatMap(data)
    hit_img = hm.heatmap(base=background, r=100)  # background为背景图片，r是半径，默认为10
    hit_img = cv2.cvtColor(np.asarray(hit_img), cv2.COLOR_RGB2BGR)  # Image格式转换成cv2格式
    overlay = image1.copy()
    alpha = 0.5  # 设置覆盖图片的透明度
    cv2.rectangle(overlay, (0, 0), (image1.shape[1], image1.shape[0]), (255, 0, 0), -1)  # 设置蓝色为热度图基本色蓝色
    image2 = cv2.addWeighted(overlay, alpha, image1, 1 - alpha, 0)  # 将背景热度图覆盖到原图
    image3 = cv2.addWeighted(hit_img, alpha, image2, 1 - alpha, 0)  # 将热度图覆盖到原图
    cv2.imshow('ru', image3)
    cv2.imwrite('rtj91.jpg', image3)
    cv2.waitKey(0)
    return image3


if __name__ == '__main__':
    # apply_heatmap('/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_results/method3_mse/7/feature_map/ret_hm_layers_resize/channel_1.jpg',
    #               [[600, 436, 30], [296, 416, 50],
    #                [270, 400, 32], [280, 426, 10], [580, 440, 30], [360, 430, 36],
    #                [540, 460, 50], [482, 469, 5],
    #                [400, 463, 8], [320, 453, 26], [200, 1140, 20], [180, 1136, 10], [120, 1130, 10],
    #                [90, 1126, 20]
    #                ])  # 数据来自通过眼动追踪技术生成的顾客凝视点中心坐标
    apply_heatmap('/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_results/method3_mse/7/feature_map_frame_20/ret_hm_layers_resize/channel_1.jpg',
                  [[149, 543, 10], [604, 563, 10], [540, 670, 10], [924, 496, 10]])
