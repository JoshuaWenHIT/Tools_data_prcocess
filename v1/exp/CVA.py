import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np



# img = cv2.imread("/home/joshuawen/Projects/Tools/data/COCO2017/sample.jpg")
# print("Input Image Size: ", img.shape)
# tensor_img = torch.from_numpy(np.transpose(img, (2, 0, 1)))
# tensor_img = torch.tensor(tensor_img, dtype=torch.float32)
# print("Input Tensor Size: ", tensor_img.shape)
# tensor_batch_img = torch.unsqueeze(tensor_img, dim=0)
# print("Input Batch Tensor Size: ", tensor_batch_img.shape)
# embedconv = nn.Sequential(
#     # feed the size of the output from backbone network
#     nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1, bias=True),
#     nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1, bias=True),
#     # get the embedding of Re-ID
#     nn.Conv2d(64, 128, kernel_size=1, stride=1, padding=0, bias=True),
#     nn.BatchNorm2d(128, momentum=0.1),
#     nn.ReLU(inplace=True),
#     nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1, bias=True),
#     nn.BatchNorm2d(128, momentum=0.1),
#     nn.ReLU(inplace=True),
#     nn.Conv2d(128, 128, kernel_size=1, stride=1, padding=0, bias=True),
#     # resize the embedding for torch.matmul
#     nn.MaxPool2d(kernel_size=2, stride=2)
# )
# embdedding_batch = embedconv(tensor_batch_img)
# print("Output Tensor Size: ", embdedding_batch.shape)
# embdedding_batch = embdedding_batch.view(1, 128, -1)
# print("Resized Tensor Size: ", embdedding_batch.shape)
# c = torch.matmul(embdedding_batch.permute(0, 2, 1), embdedding_batch)
# print("Matmul Tensor Size: ", c.shape)
# c = torch.squeeze(c, dim=0)
# # print(embdedding.shape)
# c_img = c.detach().numpy()
# # print(embdedding_img.shape)
# cv2.imwrite("/home/joshuawen/Projects/Tools/data/COCO2017/sample3.jpg", c_img)
#
#
a = torch.rand(1, 1, 2, 2)
print(a)
b = nn.functional.interpolate(a, scale_factor=2)
print(b)
# b = a.view(1, 4, 1, 2)
# print(b)
# c = b.max(dim=3)[0]
# print(c)
# print(c.shape)
# d = b.max(dim=2)[0]
# print(d)
# print(d.shape)
# e = F.softmax(d * 5, dim=2)
# print(e)
# print(e.shape)
# f = F.softmax(d, dim=2)
# print(f)
# print(f.shape)

# h = 4
# w = 4
# off_template_w = np.zeros((h, w, w), dtype=np.float32)
# off_template_h = np.zeros((h, w, h), dtype=np.float32)
# for ii in range(h):
#     for jj in range(w):
#         for i in range(h):
#             off_template_w[ii, jj, i] = i - ii
#         for j in range(w):
#             off_template_h[ii, jj, j] = j - jj
# print(off_template_w)
# m = np.reshape(off_template_w, newshape=(h * w, w))[None, :, :] * 2
# v = np.reshape(off_template_h, newshape=(h * w, h))[None, :, :] * 2
# print(m)
# print(v)
# m = torch.Tensor(m)
# print(m)
# print(m.shape)
# print(m * f)
# off_w = torch.sum(m * f, dim=2, keepdim=True)
# print(off_w)
# print(off_w.permute(0, 2, 1))
# h = 2
# w = 2
# off_template_w = np.zeros((h, w, w), dtype=np.float32)
# print(off_template_w)

# a = torch.rand(1, 3, 5)
# b = torch.rand(1, 3, 5)
# out = pearsonr(a, b)
# print(out)
# print(out.size())
