import os
import json
import cv2

f = open(os.path.join('/home/hyg/Downloads/科目四热身赛数据/', "via_region_data.json"), encoding='utf-8')
pic = json.load(f)
item = pic.keys()
pic_new = {}
i = 1
# print(str(i))
areas = []
file_handle = open('1.txt', mode='w')
for name in item:
    temp = pic[name]['filename']
    temp0 = temp.split('.png')
    filename = temp0[0] + '.txt'
    f1 = open('/home/hyg/Downloads/科目四热身赛数据/labels/' + filename)
    tr = f1.read()
    f1.close()
    tr = tr.split('\n')
    # print(tr[0])
    regions = {}
    for i in range(len(tr) - 1):
        r = tr[i]
        r = r.split(' ')
        region = {str(i): {
            "shape_attributes": {"name": "polygon", "all_points_x": [int(r[1]), int(r[3]), int(r[5]), int(r[7])],
                                 "all_points_y": [int(r[2]), int(r[4]), int(r[6]), int(r[8])]},
            "region_attributes": {"cls": r[0]}}}
        regions.update(region)
        print(regions)
        pic[name]['regions'] = regions
with open(os.path.join('/home/hyg/Downloads/科目四热身赛数据/images/', "via_region_data.json"), 'w') as f:
    json.dump(pic, f)
