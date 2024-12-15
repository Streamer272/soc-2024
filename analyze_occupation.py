import numpy as np

from analyze import analyze

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}, analyzing column 6 (sex)")
print("\t0 - work hours / week >= 10")
print("\t1 - work hours / week < 10")
print("\t2 - sport")
print("\t3 - music")
print("\t4 - other")
print("\t5 - none")
print("")


def analyze_occupation(name: str, col: np.ndarray):
    occupation_col = dataset[:, 6]
    analyze(name, [
        col[occupation_col == 0],
        col[occupation_col == 1],
        col[occupation_col == 2],
        col[occupation_col == 3],
        col[occupation_col == 4],
        col[occupation_col == 5]
    ])


analyze_occupation("gpa", dataset[:, 2])
analyze_occupation("math", dataset[:, 3])
analyze_occupation("slovak", dataset[:, 4])
analyze_occupation("english", dataset[:, 5])
