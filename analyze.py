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


def plot_violin(data, labels, Fs, ps, title):
    if not graph:
        return

    grade_names = ["Priemer", "Matematika", "Slovenčina", "Angličtina"]
    grade_name_labels = ["Priemer známok", "Známka z matematiky", "Známka zo slovenčiny", "Známka z angličtiny"]

    fig, axs = plt.subplots(2, 2)
    fig.suptitle(title)
    fig.set_size_inches(12, 9)

    for j in range(2):
        for k in range(2):
            index = j * 2 + k
            step = 1 if index > 0 else 0.5

            axs[j, k].violinplot(data[index], showmeans=True)
            axs[j, k].set_title(grade_names[index])
            axs[j, k].set_xlabel(title, fontweight="bold")
            axs[j, k].set_ylabel(grade_name_labels[index], fontweight="bold")
            axs[j, k].set_xticks(np.arange(1, len(labels) + 1), labels=labels)
            axs[j, k].set_yticks(np.arange(1, 5.01, step))

            F = round(Fs[index], 2)
            p = round(ps[index], 4)
            axs[j, k].text(0.01, 0.99, f"F-stat: {F:.2f}\np-val: {p:.4f}", ha="left", va="top", transform=axs[j, k].transAxes,
                           fontweight="bold")

            means = list([a.mean() for a in data[index]])
            for l in range(len(means)):
                mean = round(means[l], 2)
                axs[j, k].text(l + 1.05, mean + 0.05, f"{mean}")

    fig.tight_layout()
    fig.show()
    plt.show()
