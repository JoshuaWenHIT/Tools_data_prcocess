import os
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

txt_format = {'arch': 'CenterNet', 'method': 1, 'filename': 'log'}


def read_txt_to_list(txt_path):
    list = []
    try:
        f = open(txt_path, "r")  # 设置文件对象
        line = f.readline()
        # print(line)
        line = line.strip('\n')
        list.append(line)
        while line:  # 直到读取完文件
            line = f.readline()  # 读取一行文件，包括换行符
            line = line.strip('\n')  # 去掉换行符，也可以不去
            list.append(line)
        f.close()
    except FileNotFoundError:
        print("File is not found !")
    except PermissionError:
        print("You don't have permission to access this file !")

    return list


def CenterNet_log_read(txt_list):
    log_dict = {
        'train': {'time_stamp': [], 'total_time': [], 'epoch': [], 'loss': [], 'hm_loss': [], 'wh_loss': [], 'off_loss': []},
        'val': {'epoch': [], 'loss': [], 'hm_loss': [], 'wh_loss': [], 'off_loss': []}
    }
    length = len(txt_list)
    time = 0
    print("===> Model has been trained {} epochs".format(length - 1))
    if length == 0:
        print("Reading list is ERROR !")
    else:
        for i in range(length - 1):
            if txt_list[i] is '':
                print("txt_list [{}] is None !".format(i))
            else:
                txt_list_split = txt_list[i].split('|')
                split_length = len(txt_list_split)
                if split_length == 0:
                    print("Reading splt_list is ERROR !")
                else:
                    for j in range(split_length - 1):
                        if j == 0:
                            time_stamp = txt_list_split[j].split(':')[0]
                            log_dict['train']['time_stamp'].append(time_stamp)
                            epoch_num = int(txt_list_split[j].split(':')[2])
                            log_dict['train']['epoch'].append(epoch_num)
                            if epoch_num % 5 == 0:
                                log_dict['val']['epoch'].append(epoch_num)
                        elif j == 1:
                            loss = float(txt_list_split[j].split(' ')[1])
                            log_dict['train']['loss'].append(loss)
                        elif j == 2:
                            hm_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['train']['hm_loss'].append(hm_loss)
                        elif j == 3:
                            wh_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['train']['wh_loss'].append(wh_loss)
                        elif j == 4:
                            off_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['train']['off_loss'].append(off_loss)
                        elif j == 5:
                            time += float(txt_list_split[j].split(' ')[2])
                        elif j == 6:
                            loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['val']['loss'].append(loss)
                        elif j == 7:
                            hm_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['val']['hm_loss'].append(hm_loss)
                        elif j == 8:
                            wh_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['val']['wh_loss'].append(wh_loss)
                        elif j == 9:
                            off_loss = float(txt_list_split[j].split(' ')[2])
                            log_dict['val']['off_loss'].append(off_loss)
    log_dict['train']['total_time'].append(str(time) + ' min')
    print("===> Train time: {}".format(log_dict['train']['total_time'][0]))
    return log_dict


def plot_loss(txt_format, txt_path):
    txt_list = read_txt_to_list(txt_path)
    if txt_format['arch'] == 'CenterNet' and txt_format['filename'] == 'log':
        log_dict = CenterNet_log_read(txt_list)

        epoch_num_train = log_dict['train']['epoch']
        loss_train = log_dict['train']['loss']
        hm_loss_train = log_dict['train']['hm_loss']
        wh_loss_train = log_dict['train']['wh_loss']
        off_loss_train = log_dict['train']['off_loss']

        epoch_num_val = log_dict['val']['epoch']
        loss_val = log_dict['val']['loss']
        hm_loss_val = log_dict['val']['hm_loss']
        wh_loss_val = log_dict['val']['wh_loss']
        off_loss_val = log_dict['val']['off_loss']

        if txt_format['method'] == 1:
            fig = plt.figure(figsize=(7, 7))
            ax1 = fig.add_subplot(1, 1, 1)
            font = {'weight': 'bold', 'size': 14}
            legend_properties = {'weight': 'bold'}
            pl.plot(epoch_num_train, loss_train, 'b-', label=u'loss')
            pl.legend(prop=legend_properties)
            pl.plot(epoch_num_train, hm_loss_train, 'r-', label=u'hm_loss')
            pl.legend(prop=legend_properties)
            pl.plot(epoch_num_train, wh_loss_train, 'g-', label=u'wh_loss')
            pl.legend(prop=legend_properties)
            pl.plot(epoch_num_train, off_loss_train, 'darkgoldenrod', label=u'off_loss')
            pl.legend(prop=legend_properties)
            pl.xlabel(u'Epoch', fontdict=font)
            pl.ylabel(u'Loss', fontdict=font)
            plt.yticks(np.arange(0, 30, 1.0))
            plt.title('Training Loss Curves(Improved Method)', fontdict=font)
            pl.axis([0, 350, 0.000000, 30.000000])
            epoch_start = 25
            epoch_end = 350
            loss_train_start = 0.000000
            loss_train_end = 1.500000
            sx = [epoch_start, epoch_end, epoch_end, epoch_start, epoch_start]
            sy = [loss_train_start, loss_train_start, loss_train_end, loss_train_end, loss_train_start]
            pl.plot(sx, sy, "purple")
            axins = inset_axes(ax1, width=2.5, height=1.5, loc='right')
            axins.plot(epoch_num_train, loss_train, color='blue', ls='-')
            axins.plot(epoch_num_train, hm_loss_train, color='red', ls='-')
            axins.plot(epoch_num_train, wh_loss_train, color='green', ls='-')
            axins.plot(epoch_num_train, off_loss_train, color='darkgoldenrod', ls='-')
            axins.axis([25, 400, 0.000000, 1.500000])
            plt.xticks(np.arange(25, 400, 50))
            plt.yticks(np.arange(0, 1.5, 0.2))
            plt.annotate("0.439", (350, 0.438650), xycoords='data',
                         xytext=(350, 1.2),
                         arrowprops=dict(arrowstyle='->'),
                         fontproperties=legend_properties)
            plt.annotate("0.316", (350, 0.315963), xycoords='data',
                         xytext=(360, 0.8),
                         arrowprops=dict(arrowstyle='->'),
                         fontproperties=legend_properties)
            # plt.annotate("0.897", (350, 0.897477), xycoords='data',
            #              xytext=(340, 1.6),
            #              arrowprops=dict(arrowstyle='->'),
            #              fontproperties=legend_properties)
            plt.annotate("0.115", (350, 0.115254), xycoords='data',
                         xytext=(360, 0.35),
                         arrowprops=dict(arrowstyle='->'),
                         fontproperties=legend_properties)
            plt.savefig("loss_train_CenterNet_Method3_mae_2.png")
            pl.show()


plot_loss(txt_format=txt_format, txt_path='/home/joshuawen/Projects/CenterNet/exp/ctdet/pig/method3_logs_2020-12-24-14-59/log.txt')
