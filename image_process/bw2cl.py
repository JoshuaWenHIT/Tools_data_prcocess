import cv2
import numpy as np


def SetcolorR(gray):
    if gray < 127:
        return 0
    elif gray > 191:
        return 255
    else:
        return 4 * gray - 510


def SetcolorG(gray):
    if gray <= 63:
        return 254 - 4 * gray
    elif 64 <= gray <= 127:
        return (gray - 191) * 4 - 254
    elif 128 <= gray <= 191:
        return 255
    elif 192 <= gray <= 255:
        return 1022 - 4 * gray


def SetcolorB(gray):
    if 0 <= gray <= 63:
        return 255
    elif 64 <= gray <= 127:
        return 510 - 4 * gray
    elif 128 <= gray <= 255:
        return 0


def TransColor(image):
    rows = image.shape[0]
    cols = image.shape[1]
    print(rows, cols)
    Color = np.zeros((rows, cols, 3), np.uint8)
    for i in range(rows):
        for j in range(cols):
            r = 255 - SetcolorR(image[i, j])
            g = 255 - SetcolorG(image[i, j])
            b = 255 - SetcolorB(image[i, j])
            Color[i, j, 0] = r
            Color[i, j, 1] = g
            Color[i, j, 2] = b
    return Color


# image = cv2.imread('/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_results/method3_mse/7/feature_map_frame_20/ret_hm_layers_resize/channel_1.jpg')
# cv2.imshow('image', image)
# grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # print(image)
# grayImg2Color = TransColor(grayImg)
# cv2.imshow('grayImg', grayImg)
# r, g, b = cv2.split(grayImg2Color)
# cv2.imshow('Color0', r)
# cv2.imshow('Color1', g)
# cv2.imshow('Color2', b)
# cv2.imshow('grayImg2Color', grayImg2Color)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img_ori = cv2.imread('/media/joshuawen/Joshua_SSD3/Exp/PTDS_CenterTrack/img/ret_hm_layers_channel_1.jpg')
img_rgb = cv2.applyColorMap(img_ori, cv2.COLORMAP_JET)
cv2.imwrite('/media/joshuawen/Joshua_SSD3/Exp/PTDS_CenterTrack/img/RGB_ret_hm_layers_channel_1.jpg', img_rgb)
cv2.imshow('RGB', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
