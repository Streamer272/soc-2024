import numpy as np
import scipy.stats as stats

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}, analyzing column 1 (sex)")
print("\t0 - female")
print("\t1 - male")
print("")


def analyze(name: str, col: np.ndarray):
    sex_col = dataset[:, 1]
    F, p = stats.f_oneway(col[sex_col == 0], col[sex_col == 1])
    print(f"F-stats for {name}: {F}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
        return

    print("statistically significant")
    tukey_results = stats.tukey_hsd(col[sex_col == 0], col[sex_col == 1])
    print(tukey_results)


analyze("gpa", dataset[:, 2])
analyze("math", dataset[:, 3])
analyze("slovak", dataset[:, 4])
analyze("english", dataset[:, 5])
