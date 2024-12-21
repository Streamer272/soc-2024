import numpy as np

from analyze import analyze, plot_violin

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 7 (occupation)")
print("\t0 - work hours / week >= 10")
print("\t1 - work hours / week < 10")
print("\t2 - sport")
print("\t3 - music")
print("\t4 - other")
print("\t5 - none")
print("")


def analyze_occupation(name: str, col: np.ndarray):
    occupation_col = dataset[:, 7]
    data = [
        col[occupation_col == 0],
        col[occupation_col == 1],
        col[occupation_col == 2],
        col[occupation_col == 3],
        col[occupation_col == 4],
        col[occupation_col == 5]
    ]
    F, p = analyze(name, data)
    return data, F, p


data_gpa, F_gpa, p_gpa = analyze_occupation("gpa", dataset[:, 2])
data_math, F_math, p_math = analyze_occupation("math", dataset[:, 3])
data_slovak, F_slovak, p_slovak = analyze_occupation("slovak", dataset[:, 4])
data_english, F_english, p_english = analyze_occupation("english", dataset[:, 5])

plot_violin([data_gpa, data_math, data_slovak, data_english],
            ["Veľa práce", "Málo práce", "Šport", "Hudba", "Iné", "Žiadne"],
            [F_gpa, F_math, F_slovak, F_english], [p_gpa, p_math, p_slovak, p_english], "Práca alebo aktivita")
