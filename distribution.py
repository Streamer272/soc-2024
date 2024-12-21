import numpy as np
import argparse
import matplotlib.pyplot as plt
from math import floor

parser = argparse.ArgumentParser(
    prog="distribution"
)
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Display graphs")
args = parser.parse_args()
graph = args.graph

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing distribution\n")


def percent(fraction: float) -> str:
    return f"{floor(fraction * 10_000) / 100:.2f}%"


def plot_bar(x, y, title, xlabel, fix_x_labels=False):
    plt.figure(figsize=(8, 6))
    plt.bar(x, np.array(y) * 100)
    plt.ylim(0, 100)
    for i in range(len(x)):
        plt.text(i - 0.05 * len(x), y[i] * 100 + 1, percent(y[i]))
    plt.title(title)
    plt.ylabel("Percentá", fontweight="bold")
    plt.xlabel(xlabel, labelpad=5, fontweight="bold")

    if fix_x_labels:
        _, labels = plt.xticks()
        for i in range(len(labels)):
            labels[i].set_y(-(i % 2) * 0.04)
            print(labels[i])

    plt.tight_layout()
    plt.show()


grade = dataset[:, 0]
grade_dist = [
    len(grade[grade == 1]) / len(grade),
    len(grade[grade == 2]) / len(grade),
    len(grade[grade == 3]) / len(grade),
    len(grade[grade == 4]) / len(grade),
    len(grade[grade == 5]) / len(grade)
]
print("--- GRADE ---")
print(f"1st year: {percent(grade_dist[0])}")
print(f"2st year: {percent(grade_dist[1])}")
print(f"3st year: {percent(grade_dist[2])}")
print(f"4st year: {percent(grade_dist[3])}")
print(f"5st year: {percent(grade_dist[4])}")
print("")

if graph:
    plot_bar(
        ["Prvý ročník", "Druhý ročník", "Tretí ročník", "Štvrtý ročník", "Piaty ročník"],
        grade_dist,
        "Distribúcia ročníkov",
        "Ročník"
    )

sex = dataset[:, 1]
sex_dist = [
    len(sex[sex == 0]) / len(sex),
    len(sex[sex == 1]) / len(sex)
]
print("--- SEX ---")
print(f"Female: {percent(sex_dist[0])}")
print(f"Male: {percent(sex_dist[1])}")
print("")

if graph:
    plot_bar(["Ženy", "Muži"], sex_dist, "Distribúcia pohlavia", "Pohlavie")

print("--- GPA ---")
print("n/a")
print("")
# TODO: graph numerical

math = dataset[:, 3]
math_dist = [
    len(math[math == 1]) / len(math),
    len(math[math == 2]) / len(math),
    len(math[math == 3]) / len(math),
    len(math[math == 4]) / len(math),
    len(math[math == 5]) / len(math)
]
print("--- MATH ---")
print(f"1: {percent(math_dist[0])}")
print(f"2: {percent(math_dist[1])}")
print(f"3: {percent(math_dist[2])}")
print(f"4: {percent(math_dist[3])}")
print(f"5: {percent(math_dist[4])}")
print("")

if graph:
    plot_bar(["1", "2", "3", "4", "5"], math_dist, "Distribúcia známok z matematiky", "Známka")

slovak = dataset[:, 4]
slovak_dist = [
    len(slovak[slovak == 1]) / len(slovak),
    len(slovak[slovak == 2]) / len(slovak),
    len(slovak[slovak == 3]) / len(slovak),
    len(slovak[slovak == 4]) / len(slovak),
    len(slovak[slovak == 5]) / len(slovak)
]
print("--- SLOVAK ---")
print(f"1: {percent(slovak_dist[0])}")
print(f"2: {percent(slovak_dist[1])}")
print(f"3: {percent(slovak_dist[2])}")
print(f"4: {percent(slovak_dist[3])}")
print(f"5: {percent(slovak_dist[4])}")
print("")

if graph:
    plot_bar(["1", "2", "3", "4", "5"], slovak_dist, "Distribúcia známok zo slovenčiny", "Známka")

english = dataset[:, 5]
english_dist = [
    len(english[english == 1]) / len(english),
    len(english[english == 2]) / len(english),
    len(english[english == 3]) / len(english),
    len(english[english == 4]) / len(english),
    len(english[english == 5]) / len(english)
]
print("--- ENGLISH ---")
print(f"1: {percent(english_dist[0])}")
print(f"2: {percent(english_dist[1])}")
print(f"3: {percent(english_dist[2])}")
print(f"4: {percent(english_dist[3])}")
print(f"5: {percent(english_dist[4])}")
print("")

if graph:
    plot_bar(["1", "2", "3", "4", "5"], english_dist, "Distribúcia známok z angličtiny", "Známka")

ses = dataset[:, 6]
ses_dist = [
    len(ses[ses == 0]) / len(ses),
    len(ses[ses == 1]) / len(ses),
    len(ses[ses == 2]) / len(ses)
]
print("--- SES ---")
print(f"Lower: {percent(ses_dist[0])}")
print(f"Middle: {percent(ses_dist[1])}")
print(f"Upper: {percent(ses_dist[2])}")
print("")

if graph:
    plot_bar(["Nižšia trieda", "Stredná trieda", "Vyššia trieda"], ses_dist, "Distribúcia socio-ekonomických tried",
             "Socio-ekonomická trieda")

occupation = dataset[:, 7]
occupation_dist = [
    len(occupation[occupation == 0]) / len(occupation),
    len(occupation[occupation == 1]) / len(occupation),
    len(occupation[occupation == 2]) / len(occupation),
    len(occupation[occupation == 3]) / len(occupation),
    len(occupation[occupation == 4]) / len(occupation),
    len(occupation[occupation == 5]) / len(occupation)
]
print("--- OCCUPATION ---")
print(f"work hours / week >= 10: {percent(occupation_dist[0])}")
print(f"work hours / week < 10 : {percent(occupation_dist[1])}")
print(f"sport                  : {percent(occupation_dist[2])}")
print(f"music                  : {percent(occupation_dist[3])}")
print(f"other                  : {percent(occupation_dist[4])}")
print(f"none                   : {percent(occupation_dist[5])}")
print("")

if graph:
    plot_bar(["Práca 10 a viac hodín týždenne", "Práca menej ako 10 hodín týždenne", "Šport", "Hudba", "Niečo iné",
              "Žiadne"], occupation_dist, "Distribúcia práce a aktivít", "Práca alebo aktivita", True)

living = dataset[:, 8]
living_dist = [
    len(living[living == 0]) / len(living),
    len(living[living == 1]) / len(living),
    len(living[living == 2]) / len(living),
    len(living[living == 3]) / len(living),
    len(living[living == 4]) / len(living)
]
print("--- LIVING ---")
print(f"with family       : {percent(living_dist[0])}")
print(f"with family member: {percent(living_dist[1])}")
print(f"alone / roomates  : {percent(living_dist[2])}")
print(f"dorms             : {percent(living_dist[3])}")
print(f"other             : {percent(living_dist[4])}")
print("")

if graph:
    plot_bar(["S rodinou", "S rodinným príslušníkom/ou", "Sám/a alebo so spolubývajúcim/ou", "Intrák", "Iné"],
             living_dist, "Distribúcia životných situácií", "Životná situácia", True)

commute = dataset[:, 9]
commute_dist = [
    len(commute[commute == 0]) / len(commute),
    len(commute[commute == 1]) / len(commute),
    len(commute[commute == 2]) / len(commute),
    len(commute[commute == 3]) / len(commute),
    len(commute[commute == 4]) / len(commute)
]
print("--- COMMUTE ---")
print(f"dorms : {percent(commute_dist[0])}")
print(f"<= 15m: {percent(commute_dist[1])}")
print(f"<= 30m: {percent(commute_dist[2])}")
print(f"<= 1h : {percent(commute_dist[3])}")
print(f"> 1h  : {percent(commute_dist[4])}")
print("")

if graph:
    plot_bar(["Intrák", "Menej ako 15 minút", "Menej ako 30 minút", "Menej ako hodinu", "Viac ako hodinu"],
             commute_dist, "Distribúcia dochádzania", "Dochádzanie", True)

sleep = dataset[:, 10]
sleep_dist = [
    len(sleep[sleep == 0]) / len(sleep),
    len(sleep[sleep == 1]) / len(sleep),
    len(sleep[sleep == 2]) / len(sleep)
]
print("--- SLEEP ---")
print(f"short sleepers : {percent(sleep_dist[0])}")
print(f"medium sleepers: {percent(sleep_dist[1])}")
print(f"long sleepers  : {percent(sleep_dist[2])}")
print("")

if graph:
    plot_bar(["6 hodín a menej", "7 až 8 hodín", "9 a viac hodín"], sleep_dist, "Distribúcia spánku", "Dĺžka spánku")

print("--- ABSENCE ---")
print("n/a")
print("")
# TODO: graph numerical
