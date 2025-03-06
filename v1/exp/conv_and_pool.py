import torch
import torch.nn as nn

x = torch.randn(3, 8, 2, 2)
print(x)
avg_out = torch.mean(x, dim=1, keepdim=True)
print(avg_out)
max_out, _ = torch.max(x, dim=1, keepdim=True)
print(max_out)
x1 = torch.cat([avg_out, max_out], dim=1)
print(x1)
conv1 = nn.Conv2d(2, 1, kernel_size=7, padding=3, bias=False)
x2 = conv1(x1)
print(x2)
sigmoid = nn.Sigmoid()
x3 = sigmoid(x2)
print(x3)
x4 = x3 * x
print(x4)
