import numpy as np
from scipy.stats import kendalltau

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}, analyzing column 11 (absence)")
print("\tinteger value")
print("")


def analyze_absence(name: str, col: np.ndarray):
    absence_col = dataset[:, 11]
    tau, p = kendalltau(absence_col, col)
    print(f"ken-tau for {name}: {tau}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
    else:
        print("statistically significant\n")


analyze_absence("gpa", dataset[:, 2])
analyze_absence("math", dataset[:, 3])
analyze_absence("slovak", dataset[:, 4])
analyze_absence("english", dataset[:, 5])
