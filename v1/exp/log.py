import numpy as np


# d = dict()
# logs = dict()
# logs['name'] = 'joshua'
# logs['sex'] = 'male'
# print(logs)
# for k in d:
#     logs[k] = d[k]
#
# print(logs)
# print(d)

sample = np.array([1, 2, 3, 4], dtype='float32')
print(sample[None, :])
print(np.tile(sample[None, :], (40, 1)))