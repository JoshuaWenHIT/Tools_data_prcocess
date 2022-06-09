import xml.etree.ElementTree as ET
import os


# 批量修改整个文件夹所有的xml文件
def change_all_xml(xml_path):
    filelist = os.listdir(xml_path)
    # 打开xml文档
    for xmlfile in filelist:
        doc = ET.parse(xml_path + xmlfile)
        root = doc.getroot()
        sub1 = root.find('filename')  # 找到filename标签，
        sub1.text = os.path.splitext(xmlfile)[0] + '.jpg'  # 修改标签内容
        sub2 = root.find('folder')
        sub2.text = 'VOC2007'
        sub3 = root.find('path')
        sub3.text = os.path.join('data/VOCdevkit/VOC2007/JPEGImages/' + os.path.splitext(xmlfile)[0] + '.jpg')
        # sub2 = root.find('path')  # 找到filename标签，
        # sub2.text = os.path.splitext(xmlfile)[0] + '.jpg'  # 修改标签内容

        doc.write(xml_path + xmlfile)  # 保存修改
        print('{} is changed !'.format(xmlfile))


# 修改某个特定的xml文件
def change_one_xml(xml_path):  # 输入的是这个xml文件的全路径
    # 打开xml文档
    doc = ET.parse(xml_path)
    root = doc.getroot()
    sub1 = root.find('filename')  # 找到filename标签，
    sub1.text = '07_205.jpg'  # 修改标签内容
    doc.write(xml_path)  # 保存修改
    print('----------done--------')


change_all_xml('/media/ubuntu/HDD/bwh_data/150img/new_xml/')     # xml文件总路径
# xml_path = r'Z:\pycharm_projects\ssd\VOC2007\Annotations\07_205.xml'
# change_one_xml(xml_path)
