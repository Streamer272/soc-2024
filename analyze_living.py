import numpy as np

from analyze import analyze

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}, analyzing column 8 (living)")
print("\t0 - with family")
print("\t1 - with family member")
print("\t2 - alone / roomates")
print("\t3 - dorms")
print("\t4 - other")
print("")


def analyze_living(name: str, col: np.ndarray):
    occupation_col = dataset[:, 8]
    analyze(name, [
        col[occupation_col == 0],
        col[occupation_col == 1],
        col[occupation_col == 2],
        col[occupation_col == 3],
        col[occupation_col == 4]
    ])


analyze_living("gpa", dataset[:, 2])
analyze_living("math", dataset[:, 3])
analyze_living("slovak", dataset[:, 4])
analyze_living("english", dataset[:, 5])
