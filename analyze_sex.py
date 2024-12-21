import numpy as np

from analyze import analyze, plot_box

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 1 (sex)")
print("\t0 - female")
print("\t1 - male")
print("")


def analyze_sex(name: str, col: np.ndarray):
    sex_col = dataset[:, 1]
    data = [
        col[sex_col == 0],
        col[sex_col == 1]
    ]
    F, p = analyze(name, data)
    return data, F, p


data_gpa, F_gpa, p_gpa = analyze_sex("gpa", dataset[:, 2])
data_math, F_math, p_math = analyze_sex("math", dataset[:, 3])
data_slovak, F_slovak, p_slovak = analyze_sex("slovak", dataset[:, 4])
data_english, F_english, p_english = analyze_sex("english", dataset[:, 5])

plot_box([data_gpa, data_math, data_slovak, data_english], ["Female", "Male"],
         [F_gpa, F_math, F_slovak, F_english], [p_gpa, p_math, p_slovak, p_english],
         "Pohlavie", ["Priemer", "Matematika", "Slovenčina", "Angličtina"])
