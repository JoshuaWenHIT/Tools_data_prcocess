import numpy as np
import res


def cal_mean_std(score_list):
    return np.mean(score_list), np.std(score_list)


if __name__ == '__main__':
    max_score_list = res.qt_score_list['hopper-medium-expert']
    print(cal_mean_std(max_score_list))



