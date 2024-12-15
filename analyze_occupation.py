import numpy as np
import scipy.stats as stats

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}, analyzing column 6 (sex)")
print("\t0 - work hours / week >= 10")
print("\t1 - work hours / week < 10")
print("\t2 - sport")
print("\t3 - music")
print("\t4 - other")
print("\t5 - none")
print("")


def analyze(name: str, col: np.ndarray):
    occupation_col = dataset[:, 6]
    F, p = stats.f_oneway(col[occupation_col == 0], col[occupation_col == 1], col[occupation_col == 2], col[occupation_col == 3], col[occupation_col == 4], col[occupation_col == 5])
    print(f"F-stats for {name}: {F}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
        return

    print("statistically significant")
    tukey_results = stats.tukey_hsd(col[occupation_col == 0], col[occupation_col == 1], col[occupation_col == 2], col[occupation_col == 3], col[occupation_col == 4], col[occupation_col == 5])
    print(tukey_results)


analyze("gpa", dataset[:, 2])
analyze("math", dataset[:, 3])
analyze("slovak", dataset[:, 4])
analyze("english", dataset[:, 5])
