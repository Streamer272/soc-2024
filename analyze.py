from typing import List
import argparse

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Plot graph")
args = parser.parse_args()
graph = args.graph


def analyze(name: str, data: List[np.ndarray]):
    F, p = stats.f_oneway(*data)
    print(f"F-stats for {name}: {F}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
        return F, p

    print("statistically significant")
    tukey_results = stats.tukey_hsd(*data)
    print(tukey_results)

    return F, p


def plot_box(data, labels, Fs, ps, title, titles):
    if not graph:
        return

    fig, axs = plt.subplots(2, 2, sharex=True)
    fig.suptitle(title)
    fig.set_size_inches(12, 9)

    for i in range(2):
        for j in range(2):
            print(f"{i}x{j} giving {i * 2 + j}")
            axs[i, j].boxplot(data[i * 2 + j], labels=labels)
            axs[i, j].set_title(titles[i * 2 + j])

            F = round(Fs[i * 2 + j], 2)
            p = round(ps[i * 2 + j], 4)
            axs[i, j].text(0.01, 0.99, f"F-stat: {F}\np-val: {p}", ha="left", va="top", transform=axs[i, j].transAxes,
                           fontweight="bold")

            avgs = np.array([a.mean() for a in data[i * 2 + j]])
            print(avgs)

    fig.tight_layout()
    fig.show()
    plt.show()
