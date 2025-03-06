import math
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import torch.nn.functional as F


def sample_target(im, target_bb, search_area_factor, output_sz=None, mask=None):
    """ Extracts a square crop centered at target_bb box, of area search_area_factor^2 times target_bb area

    args:
        im - cv image
        target_bb - target box [x, y, w, h]
        search_area_factor - Ratio of crop size to target size
        output_sz - (float) Size to which the extracted crop is resized (always square). If None, no resizing is done.

    returns:
        cv image - extracted crop
        float - the factor by which the crop has been resized to make the crop size equal output_size
    """
    if not isinstance(target_bb, list):
        x, y, w, h = target_bb.tolist()
    else:
        x, y, w, h = target_bb
    # Crop image
    crop_sz = math.ceil(math.sqrt(w * h) * search_area_factor)

    if crop_sz < 1:
        raise Exception('Too small bounding box.')

    x1 = int(round(x + 0.5 * w - crop_sz * 0.5))
    x2 = int(x1 + crop_sz)

    y1 = int(round(y + 0.5 * h - crop_sz * 0.5))
    y2 = int(y1 + crop_sz)

    x1_pad = int(max(0, -x1))
    x2_pad = int(max(x2 - im.shape[1] + 1, 0))

    y1_pad = int(max(0, -y1))
    y2_pad = int(max(y2 - im.shape[0] + 1, 0))

    # Crop target
    im_crop = im[y1 + y1_pad:y2 - y2_pad, x1 + x1_pad:x2 - x2_pad, :]
    if mask is not None:
        mask_crop = mask[y1 + y1_pad:y2 - y2_pad, x1 + x1_pad:x2 - x2_pad]

    # Pad
    im_crop_padded = cv.copyMakeBorder(im_crop, y1_pad, y2_pad, x1_pad, x2_pad, cv.BORDER_CONSTANT)
    # deal with attention mask
    H, W, _ = im_crop_padded.shape
    att_mask = np.ones((H, W))
    end_x, end_y = -x2_pad, -y2_pad
    if y2_pad == 0:
        end_y = None
    if x2_pad == 0:
        end_x = None
    att_mask[y1_pad:end_y, x1_pad:end_x] = 0
    if mask is not None:
        mask_crop_padded = F.pad(mask_crop, pad=(x1_pad, x2_pad, y1_pad, y2_pad), mode='constant', value=0)

    if output_sz is not None:
        resize_factor = output_sz / crop_sz
        im_crop_padded = cv.resize(im_crop_padded, (output_sz, output_sz))
        att_mask = cv.resize(att_mask, (output_sz, output_sz)).astype(np.bool_)
        if mask is None:
            return im_crop_padded, resize_factor, att_mask
        mask_crop_padded = \
            F.interpolate(mask_crop_padded[None, None], (output_sz, output_sz), mode='bilinear', align_corners=False)[
                0, 0]
        return im_crop_padded, resize_factor, att_mask, mask_crop_padded

    else:
        if mask is None:
            return im_crop_padded, att_mask.astype(np.bool_), 1.0
        return im_crop_padded, 1.0, att_mask.astype(np.bool_), mask_crop_padded


if __name__ == '__main__':
    # img = cv.imread("/home/HDD/Datasets/LT/airplane/color/00000001.jpg")
    # # print(img.shape)
    # target_bbox = [601.0, 318.0, 213.0, 95.0]
    # # im_crop_padded, resize_factor, att_mask = sample_target(im=img, target_bb=target_bbox, search_area_factor=5.0)
    # im_crop_padded, resize_factor, att_mask = sample_target(im=img, target_bb=target_bbox, search_area_factor=4.0,
    #                                                         output_sz=384)
    # print(resize_factor)
    # print(im_crop_padded.shape)
    # print(att_mask[:, :, None].shape)
    # plt.subplot(121)
    # plt.imshow(cv.cvtColor(im_crop_padded, cv.COLOR_BGR2RGB))
    # plt.title("padded")
    # plt.subplot(122)
    # # plt.imshow(cv.cvtColor(att_mask[None, :], cv.COLOR_GRAY2RGB))
    # # plt.imshow(att_mask[:, :, None])
    # plt.imshow(att_mask)
    # plt.title("mask")
    # plt.savefig("search_template")
    # plt.show()
    import torch
    attn_pt = "/home/HDD/Temp/airplane_xzs/airplane_embed_seq_200.pt"
    tensor = torch.load(attn_pt, map_location=torch.device('cpu'))
    tensor_reshaped = tensor.numpy().reshape((16, 16))
    tensor_norm = (tensor_reshaped - np.min(tensor_reshaped)) / (np.max(tensor_reshaped) - np.min(tensor_reshaped))
    # data = np.random.rand(16, 16)
    plt.imshow(tensor_norm, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('16x16 Heatmap')
    plt.axis('off')
    plt.savefig('./heatmap.png')
    plt.show()
