import numpy as np

from analyze import analyze

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 6 (ses)")
print("\t0 - lower class")
print("\t1 - middle class")
print("\t2 - upper class")
print("")


def analyze_ses(name: str, col: np.ndarray):
    sex_col = dataset[:, 6]
    analyze(name, [
        col[sex_col == 0],
        col[sex_col == 1],
        col[sex_col == 2]
    ])


analyze_ses("gpa", dataset[:, 2])
analyze_ses("math", dataset[:, 3])
analyze_ses("slovak", dataset[:, 4])
analyze_ses("english", dataset[:, 5])
