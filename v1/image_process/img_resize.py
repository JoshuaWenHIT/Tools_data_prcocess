import os
import cv2


def resize_img(DATADIR, data_k, img_size):
    w = img_size[0]
    h = img_size[1]
    '''设置目标像素大小，此处设为300'''
    path = os.path.join(DATADIR, data_k)
    # 返回path路径下所有文件的名字，以及文件夹的名字，
    img_list = os.listdir(path)

    for i in img_list:
        if i.endswith('.jpg'):
            # 调用cv2.imread读入图片，读入格式为IMREAD_COLOR
            img_array = cv2.imread((path + '/' + i), cv2.IMREAD_COLOR)
            # 调用cv2.resize函数resize图片
            new_array = cv2.resize(img_array, (w, h), interpolation=cv2.INTER_CUBIC)
            img_name = str(i)
            '''生成图片存储的目标路径'''
            save_path = path + '_resize/'
            if os.path.exists(save_path):
                print(i)
                '''调用cv.2的imwrite函数保存图片'''
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)
            else:
                os.mkdir(save_path)
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)


def resize_one_image(img_path, img_size):
    w = img_size[0]
    h = img_size[1]
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_resize = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite(img_path, img_resize)
    cv2.imwrite("/media/joshuawen/Joshua_SSD3/Exp/PTDS_CenterTrack/img/Resize_RGB_ret_hm_layers_channel_1.jpg", img_resize)


if __name__ == '__main__':
    # 设置图片路径
    # DATADIR = "/media/joshuawen/SSD_2/Paper/CenterCounter/image_mat/exp/video_results/method1/7/feature_map_frame_318/"
    # data_k = ['layer0_conv1', 'layer0_bn1', 'layer0_relu1', 'layer0_pool1',
    #           'layer1', 'layer2', 'layer3', 'layer4',
    #           'deconv_layers',
    #           'ret_hm_layers', 'ret_wh_layers', 'ret_reg_layers']
    # # 需要修改的新的尺寸
    # img_size = [1024, 1024]
    # for data_k_i in data_k:
    #     resize_img(DATADIR, data_k_i, img_size)
    resize_one_image("/media/joshuawen/Joshua_SSD3/Exp/PTDS_CenterTrack/img/RGB_ret_hm_layers_channel_1.jpg", (1920, 1080))
