import os


SRC_PATH = "/home/joshuawen/WorkSpace/datasets/RSOD/train/labels"
DST_PATH = "/home/joshuawen/WorkSpace/datasets/RSOD/train/labels-new"
for txt in sorted(os.listdir(SRC_PATH)):
    if 'aircraft' in txt:
        continue
    with open(os.path.join(SRC_PATH, txt), 'r') as f:
        with open(os.path.join(DST_PATH, txt), 'w') as new_f:
            for line in f.readlines():
                # label = line.split(' ')
                # new_line = '0 ' + label[1] + ' ' + label[2] + ' ' + label[3] + ' ' + label[4]
                # new_f.write(new_line)
                new_f.write('')


