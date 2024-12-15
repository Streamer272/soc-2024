import numpy as np

from analyze import analyze

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 1 (sex)")
print("\t0 - female")
print("\t1 - male")
print("")


def analyze_sex(name: str, col: np.ndarray):
    sex_col = dataset[:, 1]
    analyze(name, [
        col[sex_col == 0],
        col[sex_col == 1]
    ])


analyze_sex("gpa", dataset[:, 2])
analyze_sex("math", dataset[:, 3])
analyze_sex("slovak", dataset[:, 4])
analyze_sex("english", dataset[:, 5])
