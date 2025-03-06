import numpy as np
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from rliable import library as rly
from rliable import metrics
from rliable import plot_utils
#
#
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4.4, 3.4))
#
# mean, std = 0.3910, 0.0072
# mult = 1.2
# fn = lambda x: np.minimum(mult * (1 - scipy.stats.norm.cdf(x, loc=mean, scale=std)), 1.0)
# inv_fn = lambda y: scipy.stats.norm.ppf(1 - (y / mult), loc=mean, scale=std)
#
# x = np.linspace(0.0, 2.0 , 200)
# y = fn(x)
#
# ax.plot(x, y)
#
#
# ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
#
# ax.tick_params(labelsize='x-large')
# ax.set_xlim(left=x[0], right=x[-1])
# ax.set_ylim(0.0, 1.0)
#
# y1 = y[(y>=0.25) & (y <=0.75)]
# x1 = [a for a, t in zip(x, y) if (t <= 0.75) and (t >=0.25)]
#
# ax.fill_between(x[x<=1], 1, y[x<=1], color='orange', label='Optimality Gap')
#
# x_25, x_75 = inv_fn(0.75), inv_fn(0.25)
#
#
# ax.axhline(y=0.25, xmax=x_75/x[-1], linestyle=":", color='black')
# ax.axhline(y=0.75, xmax=x_25/x[-1], linestyle=":", color='black')
# ax.axvline(x=1.0, ymin=fn(1.0), linestyle="--", color='black')
#
# ax.axvline(x=x_25, ymax=0.75, linestyle=":", color='black')
# ax.axvline(x=x_75, ymax=0.25, linestyle=":", color='black')
# cond = (x >= x_25) & (x <= x_75)
# ax.fill_between(x[cond], y[cond], 0.0, color='red',
#                 label='IQM')
# ax.set_ylabel(r'P$(X > \tau)$', fontsize='xx-large')
# ax.set_xlabel('Normalized score ' + r'$(\tau$)', fontsize='xx-large')
#
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# plt.legend(fontsize='x-large', loc='upper right',
#            fancybox=True, bbox_to_anchor=(1.13, 1.0))
# plt.show()

# against other algorithms

# pairs = [['IDAAC', 'PPG'], ['IDAAC', 'UCB-DrAC'], ['IDAAC', 'PPO'],
#          ['PPG', 'PPO'], ['UCB-DrAC', 'PLR'],
#          ['PLR', 'MixReg'], ['UCB-DrAC', 'MixReg'],  ['MixReg', 'PPO']]
#
# procgen_algorithm_pairs = {}
# for pair in pairs[::-1]:
#   d1 = norm_procgen_data['Min-Max'][pair[0]]
#   d2 = norm_procgen_data['Min-Max'][pair[1]]
#   # d_concat = np.concatenate((d1, d2), axis=-1)
#   procgen_algorithm_pairs['_'.join(pair)] = (d1, d2)
#
# probabilities, probability_cis = rly.get_interval_estimates(
#     procgen_algorithm_pairs, metrics.probability_of_improvement, reps=2000)
#
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(3.7, 2.1))
# h = 0.6
#
# ax2 = ax.twinx()
# colors = sns.color_palette('colorblind')
#
# for i, (pair, p) in enumerate(probabilities.items()):
#     (l, u), p = probability_cis[pair], p
#
#     ax.barh(y=i, width=u - l, height=h,
#             left=l, color=colors[i],
#             alpha=0.75, label=pair[0])
#     ax2.barh(y=i, width=u - l, height=h,
#              left=l, color=colors[i],
#              alpha=0.0, label=pair[1])
#     ax.vlines(x=p, ymin=i - 7.5 * h / 16, ymax=i + (6 * h / 16),
#               color='k', alpha=0.85)
#
# ax.set_yticks(list(range(len(pairs))))
# ax2.set_yticks(range(len(pairs)))
# pairs = [x.split('_') for x in probabilities.keys()]
# ax2.set_yticklabels([pair[1] for pair in pairs], fontsize='large')
# ax.set_yticklabels([pair[0] for pair in pairs], fontsize='large')
# ax2.set_ylabel('Algorithm Y', fontweight='bold', rotation='horizontal', fontsize='x-large')
# ax.set_ylabel('Algorithm X', fontweight='bold', rotation='horizontal', fontsize='x-large')
# ax.set_xticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
# ax.yaxis.set_label_coords(-0.2, 1.0)
# ax2.yaxis.set_label_coords(1.15, 1.13)
# decorate_axis(ax, wrect=5)
# decorate_axis(ax2, wrect=5)
#
# ax.tick_params(axis='both', which='major', labelsize='x-large')
# ax2.tick_params(axis='both', which='major', labelsize='x-large')
# ax.set_xlabel('P(X > Y)', fontsize='xx-large')
# ax.grid(axis='x', alpha=0.2)
# plt.subplots_adjust(wspace=0.05)
# ax.spines['left'].set_visible(False)
# ax2.spines['left'].set_visible(False)
#
# plt.show()


# Probability of Improvement
colors = sns.color_palette('colorblind')
xlabels = ['EDT', 'Reinformer', 'AE-RvS']
color_idxs = [0, 3, 4]
ATARI_100K_COLOR_DICT = dict(zip(xlabels, [colors[idx] for idx in color_idxs]))

algorithms = ['EDT', 'Reinformer', 'AE-RvS']
our_algorithm = 'AE-RvS' #@param ['SimPLe', 'DER', 'OTR', 'CURL', 'DrQ(ε)', 'SPR']
score_dict = {
    'EDT': np.array([[107.8, 107.8, 107.8, 107.8, 107.8],
                     [63.5, 63.5, 63.5, 63.5, 63.5]]),
    'Reinformer': np.array([[107.82, 107.82, 107.82, 107.82, 107.82],
                            [81.60, 81.60, 81.60, 81.60, 81.60]]),
    'AE-RvS' : np.array([[112.31977778048, 111.343219209436, 111.463448192529, 111.537561575314, 111.291290274559],
                         [89.402797002872, 87.2899553056887, 76.1215663075499, 86.6900381152978, 79.692988016934]]),
}
# score_dict = {
#     'EDT': {
#         'task-1': [107.8, 107.8, 107.8, 107.8, 107.8],
#
#     },
#     'Reinformer': {
#         'task-1': [107.82, 107.82, 107.82, 107.82, 107.82],
#     },
#     'AE-RvS' : {
#         'task-1': [112.31977778048, 111.343219209436, 111.463448192529, 111.537561575314, 111.291290274559],
#     }
# }
all_pairs =  {}
for alg in (algorithms):
  if alg == our_algorithm:
    continue
  pair_name = f'{our_algorithm}_{alg}'
  all_pairs[pair_name] = (
      score_dict[our_algorithm], score_dict[alg])

probabilities, probability_cis = {}, {}
reps = 5
probabilities, probability_cis = rly.get_interval_estimates(
    all_pairs, metrics.probability_of_improvement, reps=reps)

fig, ax = plt.subplots(figsize=(15, 15))
h = 0.6
algorithm_labels = []

for i, (alg_pair, prob) in enumerate(probabilities.items()):
  _, alg1 = alg_pair.split('_')
  algorithm_labels.append(alg1)
  (l, u) = probability_cis[alg_pair]
  ax.barh(y=i, width=u-l, height=h,
          left=l, color=ATARI_100K_COLOR_DICT[alg1],
          alpha=0.75)
  ax.vlines(x=prob, ymin=i-7.5 * h/16, ymax=i+(6*h/16),
            color='k', alpha=0.85)
ax.set_yticks(range(len(algorithm_labels)))
ax.set_yticklabels(algorithm_labels)


ax.set_title(fr'P({alg} > $Y$)', size='xx-large')
plot_utils._annotate_and_decorate_axis(ax, labelsize='xx-large', ticklabelsize='xx-large')
ax.set_ylabel(r'Algorithm $Y$', size='xx-large')
ax.xaxis.set_major_locator(MaxNLocator(4))
fig.subplots_adjust(wspace=0.25, hspace=0.45)

plt.show()