import numpy as np

from analyze import analyze, plot_violin

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 8 (living)")
print("\t0 - with family")
print("\t1 - with family member")
print("\t2 - alone / roomates")
print("\t3 - dorms")
print("\t4 - other")
print("")


def analyze_living(name: str, col: np.ndarray):
    occupation_col = dataset[:, 8]
    data = [
        col[occupation_col == 0],
        col[occupation_col == 1],
        col[occupation_col == 2],
        col[occupation_col == 3],
        col[occupation_col == 4]
    ]
    F, p = analyze(name, data)
    return data, F, p


data_gpa, F_gpa, p_gpa = analyze_living("gpa", dataset[:, 2])
data_math, F_math, p_math = analyze_living("math", dataset[:, 3])
data_slovak, F_slovak, p_slovak = analyze_living("slovak", dataset[:, 4])
data_english, F_english, p_english = analyze_living("english", dataset[:, 5])

plot_violin([data_gpa, data_math, data_slovak, data_english],
            ["Rodina", "Príslušník/čka", "Sám/a | spolu", "Intrák", "Iné"], [F_gpa, F_math, F_slovak, F_english],
            [p_gpa, p_math, p_slovak, p_english], "Životná situácia")
