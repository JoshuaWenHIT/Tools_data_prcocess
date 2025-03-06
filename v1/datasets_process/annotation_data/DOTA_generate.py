import os


def txt_to_DOTA(source_path, target_path):
    for root, dirs, files in os.walk(source_path):
        for file in files:
            print(file)
            with open(os.path.join(target_path, file), 'w') as w:
                w.write('imagesource:HJJ\ngsd:0.15\n')
            with open(os.path.join(root, file), 'r') as r:
                label = r.readlines()
                for i in range(len(label)):
                    cls = int(label[i].split(' ')[0])
                    print(cls)
                    x1 = format(int(label[i].split(' ')[1]), '.1f')
                    y1 = format(int(label[i].split(' ')[2]), '.1f')
                    x2 = format(int(label[i].split(' ')[3]), '.1f')
                    y2 = format(int(label[i].split(' ')[4]), '.1f')
                    x3 = format(int(label[i].split(' ')[5]), '.1f')
                    y3 = format(int(label[i].split(' ')[6]), '.1f')
                    x4 = format(int(label[i].split(' ')[7]), '.1f')
                    y4 = format(int(label[i].split(' ')[8]), '.1f')
                    new_label = str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(x3) + ' ' + str(y3) + ' ' + str(x4) + ' ' + str(y4) + ' ' + str(cls) + ' ' + str(1) + '\n'
                    print(new_label)
                    with open(os.path.join(target_path, file), 'a') as w:
                        w.write(new_label)
                w.close()
            r.close()


if __name__ == '__main__':
    source_path = '/media/joshuawen/Datasets/Datasets/HJJ_4_Pre/train/labels'
    target_path = '/media/joshuawen/Datasets/Datasets/HJJ_DOTA_Pre/train/labelTxt'
    txt_to_DOTA(source_path=source_path, target_path=target_path)
