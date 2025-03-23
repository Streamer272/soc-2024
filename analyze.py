from typing import List
import itertools
import argparse

import numpy as np
import pandas as pd
import scipy.stats as stats
import scikit_posthocs as sp
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Plot graph")
parser.add_argument("-s", "--save", default="", help="Graph save location")
args = parser.parse_args()
graph = args.graph
save = args.save

colors = ["lightblue", "lightgreen", "lightcoral"]
edge_colors = ["blue", "green", "red"]


# source: mostly ChatGPT (ain't no way i'm writing this shit myself)
def analyze(name: str, data: List[np.ndarray]):
    filtered_data = []
    group_names = []
    all_values = []
    for index, item in enumerate(data):
        numeric_data = [x for x in item if isinstance(x, (int, float))]
        if len(numeric_data) > 5:
            filtered_data.append(numeric_data)
            group_names.append(chr(65 + index))
            all_values.extend(numeric_data)
        else:
            print(f"Data group at index {index} removed due to insufficient size ({len(numeric_data)})")

    if len(filtered_data) < 2:
        print(f"Insufficient number of groups for Kruskal-Wallis test in {name}")
        return None, None

    # Kruskal-Wallis Test
    F, p = stats.kruskal(*filtered_data)
    print(f"\nF-stats for {name}: {F:.8f}")
    print(f"p-value for {name}: {p:.8f}")

    if p > 0.05:
        print("statistically insignificant\n")
        return F, p

    print("statistically significant")

    # Post-Hoc Dunn Test (Bonferroni-adjusted p-values)
    all_ranks = stats.rankdata(all_values)  # Rank all values together
    group_ranks = [all_ranks[start:start + len(group)] for start, group in
                   zip(np.cumsum([0] + [len(g) for g in filtered_data[:-1]]), filtered_data)]
    posthoc_results = sp.posthoc_conover(filtered_data, p_adjust='bonferroni')

    results = []
    total_sample_size = len(all_values)
    for group1, group2 in itertools.combinations(group_names, 2):
        idx1 = group_names.index(group1)
        idx2 = group_names.index(group2)

        mean_rank_1 = np.mean(group_ranks[idx1])
        mean_rank_2 = np.mean(group_ranks[idx2])
        rank_diff = mean_rank_1 - mean_rank_2

        n1 = len(filtered_data[idx1])
        n2 = len(filtered_data[idx2])

        # Effect size (Rank-Biserial Correlation)
        z_stat = rank_diff / np.sqrt((n1 + n2) * (n1 * n2) / total_sample_size)
        effect_size = z_stat / np.sqrt(total_sample_size)

        # Mean difference
        mean_diff = np.mean(filtered_data[idx1]) - np.mean(filtered_data[idx2])

        # Median difference
        median_diff = np.median(filtered_data[idx1]) - np.median(filtered_data[idx2])

        # Post-Hoc Dunn p-value
        p_value = posthoc_results.loc[idx1 + 1, idx2 + 1]

        results.append({
            "Skupina 1": group1,
            "Skupina 2": group2,
            "Veľkosť účinku": f"{effect_size:.4f}",
            "Rozdiel priemerov": f"{mean_diff:.4f}",
            "Rozdiel mediánov": f"{median_diff:.4f}",
            "Post-Hoc p-hodnota": f"{p_value:.4f}"
        })

    results_df = pd.DataFrame(results, dtype="object")
    print("\nSummary Table of Effect Size, Mean, and Median Differences:")
    print(results_df.to_markdown(index=False, tablefmt="github", disable_numparse=True))
    print("")

    return F, p


def plot_violin(data, labels, Fs, ps, title):
    if not graph:
        return

    grade_names = ["Priemer", "Matematika", "Slovenčina", "Angličtina"]
    grade_name_labels = ["Priemer známok", "Známka z matematiky", "Známka zo slovenčiny", "Známka z angličtiny"]

    fig, axs = plt.subplots(2, 2)
    fig.suptitle(title, fontsize=18)
    fig.set_size_inches(12, 9)

    for j in range(2):
        for k in range(2):
            index = j * 2 + k
            step = 1 if index > 0 else 0.5

            parts = axs[j, k].violinplot(data[index], showmedians=True, showmeans=True)
            axs[j, k].set_title(grade_names[index], fontsize=16)
            axs[j, k].set_xlabel(title, fontweight="bold", fontsize=14)
            axs[j, k].set_ylabel(grade_name_labels[index], fontweight="bold", fontsize=14)

            # q1-q3 lines
            for ind, vec in enumerate(data[index]):
                quartile1, median, quartile3 = np.percentile(vec, [25, 50, 75])
                if quartile1 == quartile3:
                    if quartile1 >= 0.1:
                        quartile1 -= 0.1
                    if quartile3 <= max(vec) - 0.1:
                        quartile3 += 0.1
                axs[j, k].vlines(ind + 1, quartile1, quartile3, color="gray", linewidths=3)

            axs[j, k].set_xticks(np.arange(1, len(labels) + 1), labels=labels)
            axs[j, k].set_yticks(np.arange(1, 5.01, step))

            parts["cmeans"].set_color("red")
            parts["cmedians"].set_color("green")

            for i, part in enumerate(parts["bodies"]):
                part.set_facecolor(colors[i % len(colors)])
                part.set_edgecolor(edge_colors[i % len(edge_colors)])

            F = Fs[index]
            p = ps[index]
            axs[j, k].text(0.01, 0.99, f"F-stat: {F:.4f}\np-val: {p:.4f}", ha="left", va="top",
                           transform=axs[j, k].transAxes,
                           fontweight="bold",
                           fontsize=12)
            axs[j, k].text(0.99, 0.99,
                           f"Na ľavo - priemer (červená)\nNa pravo - medián (zelená)\nSivá - medzi kvartilom 1 a 3",
                           ha="right",
                           va="top",
                           transform=axs[j, k].transAxes,
                           fontsize=12)

            medians = list([np.median(a) for a in data[index]])
            means = list([a.mean() for a in data[index]])
            for l in range(len(data[index])):
                median = medians[l]
                mean = means[l]
                # left - mean, right - median
                axs[j, k].text(l + 1.13, median - 0.05, f"{median:.2f}", color="green", fontsize=12, fontweight="bold")
                axs[j, k].text(l + 0.87 - len(labels) * 0.065, mean - 0.05, f"{mean:.2f}", color="red", fontsize=12, fontweight="bold")

            if p < 0.05:
                axs[j, k].set_facecolor("#ffff99")

    fig.tight_layout()
    if save != "":
        plt.savefig(save)
    else:
        plt.show()
