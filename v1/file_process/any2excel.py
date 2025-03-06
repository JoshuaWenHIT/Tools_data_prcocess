import copy
import os

import pandas as pd


# def sort_key(s):
#     if s.startswith('_'):
#         s = s[1:]
#     return s.split('_')[0], int(s.split('_')[1].split('.')[0])
#
#
# name_list = ['train_set', 'val_set']
# file_list = []
# temp_list = []
# flags = ['train', 'val']
# for flag in flags:
#     DIR_PATH = "/home/joshuawen/WorkSpace/datasets/RSOD/{}/images".format(flag)
#     temp_list = sorted(os.listdir(DIR_PATH), key=sort_key)
#     file_list.append(temp_list)
# # out = pd.DataFrame(columns=name_list, data=file_list)
# out = pd.DataFrame(
#     {
#         name_list[1]: file_list[1]
#     }
# )
# out.to_csv("/home/joshuawen/WorkSpace/datasets/RSOD/sat.csv", index=False)


# from openpyxl import load_workbook
#
#
# wb = load_workbook("/home/joshuawen/Personal/Doctor/MyResearch/CV_RL/review/temp.xlsx")
# col_name = []
# col_mix = []
# col_single = []
# col_overgt_mix = []
# col_overgt_single = []
# sheet = wb.worksheets[0]
# for col in sheet['A']:
#     col_name.append(col.value)
# for col in sheet['B']:
#     col_mix.append(col.value)
# for col in sheet['C']:
#     col_single.append(col.value)
# for col in sheet['D']:
#     col_overgt_mix.append(col.value)
# for col in sheet['E']:
#     col_overgt_single.append(col.value)
#
# index_list_a = []
# index_list_b = []
# for index, value in enumerate(col_mix):
#     if value:
#         # print(index)
#         index_list_a.append(index)
# for index, value in enumerate(col_single):
#     if value:
#         # print(index)
#         index_list_b.append(index)
# index_list_a.reverse()
# index_list_b.reverse()
# col_name_a = copy.deepcopy(col_name)
# col_name_b = copy.deepcopy(col_name)
# for index in index_list_a:
#     col_name_a.pop(index)
# for index in index_list_b:
#     col_name_b.pop(index)
# # print(col_name)
# print(len(col_name))
# # print(col_name_a)
# print(len(col_name_a))
# # print(col_name_b)
# print(len(col_name_b))
#
# common_list = sorted(list(set(col_name_a).intersection(set(col_name_b))))
# print(common_list)
# print(len(common_list))
