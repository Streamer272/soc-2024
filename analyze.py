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


def plot_box(data, labels, Fs, ps, title):
    if not graph:
        return

    titles = ["Priemer", "Matematika", "Slovenčina", "Angličtina"]

    fig, axs = plt.subplots(2, 2, sharex=True)
    fig.suptitle(title)
    fig.set_size_inches(12, 9)

    for j in range(2):
        for k in range(2):
            index = j * 2 + k
            axs[j, k].boxplot(data[index], labels=labels)
            axs[j, k].set_title(titles[index])

            if index > 0:
                axs[j, k].set_yticks(np.arange(1, 6, 1))

            F = round(Fs[index], 2)
            p = round(ps[index], 4)
            axs[j, k].text(0.01, 0.99, f"F-stat: {F}\np-val: {p}", ha="left", va="top", transform=axs[j, k].transAxes,
                           fontweight="bold")

            medians = np.array([np.median(a) for a in data[j * 2 + k]])
            print(medians)  # TODO: add to graph

    fig.tight_layout()
    fig.show()
    plt.show()
