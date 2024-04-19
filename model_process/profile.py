import torch
from thop import profile

model_path = ''
device = torch.device('cuda')
model_dict = torch.load(model_path, map_location=lambda storage, loc: storage.cuda(device))
