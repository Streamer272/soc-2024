import argparse

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Plot graph")
parser.add_argument("-s", "--save", default="", help="Graph save location")
args = parser.parse_args()
graph = args.graph
save = args.save

colors = ["lightblue", "lightgreen", "lightcoral"]
edge_colors = ["blue", "green", "red"]

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 11 (absence)")
print("\tinteger value")
print("")


def analyze_absence(name: str, col: np.ndarray):
    absence_col = dataset[:, 11]
    tau, p = stats.kendalltau(absence_col, col)
    print(f"ken-tau for {name}: {tau}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
    else:
        print("statistically significant\n")

    return (absence_col, col), tau, p


data_gpa, tau_gpa, p_gpa = analyze_absence("gpa", dataset[:, 2])
data_math, tau_math, p_math = analyze_absence("math", dataset[:, 3])
data_slovak, tau_slovak, p_slovak = analyze_absence("slovak", dataset[:, 4])
data_english, tau_english, p_english = analyze_absence("english", dataset[:, 5])
data = [data_gpa, data_math, data_slovak, data_english]
taus = [tau_gpa, tau_math, tau_slovak, tau_english]
ps = [p_gpa, p_math, p_slovak, p_english]

if not graph:
    exit(0)

grade_names = ["Priemer", "Matematika", "Slovenčina", "Angličtina"]
grade_name_labels = ["Priemer známok", "Známka z matematiky", "Známka zo slovenčiny", "Známka z angličtiny"]

fig, axs = plt.subplots(2, 2)
fig.suptitle("Absencia")
fig.set_size_inches(12, 9)

for j in range(2):
    for k in range(2):
        index = j * 2 + k
        step = 1 if index > 0 else 0.5

        if index == 0:
            x = dataset[:, 11]  # absence
            y = dataset[:, 2]  # gpa
            axs[j, k].scatter(x, y)
            axs[j, k].set_xlabel("Počet vymeškaných hodín")
            axs[j, k].set_ylabel(grade_name_labels[index])

            # trendline
            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)

            axs[j, k].plot(x, p(x), color="gray")
        else:
            current = list([data[index][0][data[index][1] == i + 1] for i in range(5)])  # i wanna kms
            # data[index][0] = absence
            # data[index][1] = grade
            # data[index][0][where this specific grade] -> absences for that sepcific grade
            # iterate 1 through 5 and plug into ^^

            parts = axs[j, k].violinplot(list([x if len(x) else [0] for x in current]), showmeans=True,
                                         showmedians=True)
            axs[j, k].set_xticks(np.arange(1, 6), labels=["1", "2", "3", "4", "5"])
            axs[j, k].set_xlabel(grade_name_labels[index])
            axs[j, k].set_ylabel("Počet vymeškaných hodín")

            # q1-q3 lines
            for ind, vec in enumerate(current):
                if len(vec) == 0:
                    continue
                quartile1, median, quartile3 = np.percentile(vec, [25, 50, 75])
                print(quartile1, median, quartile3)
                axs[j, k].vlines(ind + 1, quartile1, quartile3, color="gray", linewidths=3)

            parts["cmeans"].set_color("red")
            parts["cmedians"].set_color("green")

            for i, part in enumerate(parts["bodies"]):
                part.set_facecolor(colors[i % len(colors)])
                part.set_edgecolor(edge_colors[i % len(edge_colors)])

        axs[j, k].set_title(grade_names[index])

        tau = taus[index]
        p = ps[index]
        axs[j, k].text(0.01, 0.99, f"Tau τ: {tau:.4f}\np-val: {p:.4f}", ha="left", va="top",
                       transform=axs[j, k].transAxes,
                       fontweight="bold")

        if index:
            axs[j, k].text(0.99, 0.99,
                           f"Na ľavo - priemer (červená)\nNa pravo - medián (zelená)\nSivá - medzi kvartilom 1 a 3",
                           ha="right",
                           va="top",
                           transform=axs[j, k].transAxes)

            current = list([data[index][0][data[index][1] == i + 1] for i in range(5)])  # i wanna kms
            medians = list([np.median(a) if len(a) else -1 for a in current])
            means = list([a.mean() if len(a) else -1 for a in current])
            for l in range(len(current)):
                median = medians[l]
                mean = means[l]
                # left - mean, right - median
                if median >= 0:
                    axs[j, k].text(l + 1.14, median - 5, f"{median:.2f}", color="green", ha="left")
                if mean >= 0:
                    axs[j, k].text(l + 0.85, mean - 5, f"{mean:.2f}", color="red", ha="right")

fig.tight_layout()
if save != "":
    plt.savefig(save)
else:
    plt.show()
