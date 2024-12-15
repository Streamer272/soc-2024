import numpy as np

from analyze import analyze

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 10 (sleep)")
print("\t0 - short sleepers")
print("\t1 - medium sleepers")
print("\t2 - long sleepers")
print("")


def analyze_ses(name: str, col: np.ndarray):
    sex_col = dataset[:, 10]
    analyze(name, [
        col[sex_col == 0],
        col[sex_col == 1],
        col[sex_col == 2]
    ])


analyze_ses("gpa", dataset[:, 2])
analyze_ses("math", dataset[:, 3])
analyze_ses("slovak", dataset[:, 4])
analyze_ses("english", dataset[:, 5])
