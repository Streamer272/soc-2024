import numpy as np

from analyze import analyze, plot_box

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing column 6 (ses)")
print("\t0 - lower class")
print("\t1 - middle class")
print("\t2 - upper class")
print("")


def analyze_ses(name: str, col: np.ndarray):
    sex_col = dataset[:, 6]
    data = [
        col[sex_col == 0],
        col[sex_col == 1],
        col[sex_col == 2]
    ]
    F, p = analyze(name, data)
    return data, F, p


data_gpa, F_gpa, p_gpa = analyze_ses("gpa", dataset[:, 2])
data_math, F_math, p_math = analyze_ses("math", dataset[:, 3])
data_slovak, F_slovak, p_slovak = analyze_ses("slovak", dataset[:, 4])
data_english, F_english, p_english = analyze_ses("english", dataset[:, 5])

plot_box([data_gpa, data_math, data_slovak, data_english], ["Nižšia trieda", "Stredná trieda", "Vyššia trieda"],
         [F_gpa, F_math, F_slovak, F_english], [p_gpa, p_math, p_slovak, p_english], "Socio-ekonomická trieda")
