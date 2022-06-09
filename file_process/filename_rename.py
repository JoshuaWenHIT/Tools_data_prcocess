from xml.etree.ElementTree import ElementTree
from os import walk, path
import cv2
import os


def read_xml(in_path):
    """
    read and analyze xml file
    :param in_path: the input path of xml file
    :return: the ElementTree of xml file
    """
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def write_xml(tree, out_path):
    """
    write ElementTree to xml file
    :param tree: the ElementTree
    :param out_path: the output path of xml file
    :return: None
    """
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def get_path_prex(rootdir):
    """
    get path and filename in the root directory
    :param rootdir: the root path of directory
    :return: data_path: the path of file
             prefixs: filename
    """
    data_path = []
    prefixs = []
    for root, dirs, files in walk(rootdir, topdown=True):
        for name in files:
            pre, ending = path.splitext(name)
            if ending != ".xml":
                continue
            else:
                data_path.append(path.join(root, name))
                prefixs.append(pre)

    return data_path, prefixs


if __name__ == "__main__":

    # build files which will be used in VOC2007
    # if not os.path.exists("Annotations"):
    #     os.mkdir("Annotations")
    # if not os.path.exists("JPEGImages"):
    #     os.mkdir("JPEGImages")
    start_serial_number = 18631
    xml_paths, prefixs = get_path_prex('/media/ubuntu/HDD/bwh_data/150img/xml')

    for i in range(len(xml_paths)):
        # rename and save the corresponding xml
        tree = read_xml(xml_paths[i])
        # save output xml, 000001.xml
        write_xml(tree, '/media/ubuntu/HDD/bwh_data/150img/new_xml/{}.xml'.format("%06d" % (i + start_serial_number)))
        print('{}.xml'.format("%06d" % (i + start_serial_number)))

        # rename and save the corresponding image
        img_pre = prefixs[i] + ".jpg"
        root = '/media/ubuntu/HDD/bwh_data/150img/img'
        img_path = path.join(root, img_pre)
        img = cv2.imread(img_path)
        # save output jpg, 000001.jpg
        cv2.imwrite('/media/ubuntu/HDD/bwh_data/150img/new_img/{}.jpg'.format("%06d" % (i + start_serial_number)), img)
        print('{}.jpg'.format("%06d" % (i + start_serial_number)))
