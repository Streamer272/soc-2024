import numpy as np
import argparse
import matplotlib.pyplot as plt
from math import floor

parser = argparse.ArgumentParser(
    prog="distribution"
)
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Display graphs")
parser.add_argument("-s", "--save", action="store_true", default=False, help="Save graphs")
args = parser.parse_args()
graph = args.graph
save = args.save
graph_index = 1

dataset = np.load("clean.npy")
print(f"dataset shape: {dataset.shape}; analyzing distribution\n")


def percent(fraction: float) -> str:
    return f"{floor(fraction * 10_000) / 100:.2f}%"


def plot_pie(data, labels, title, explode=None):
    global graph_index
    if not graph:
        return

    i = 0
    while i < len(data):
        if data[i] == 0:
            data.pop(i)
            labels.pop(i)
        else:
            i += 1

    plt.figure(figsize=(12, 9))
    plt.pie(np.array(data), labels=labels, autopct=lambda pct: percent(pct / 100), explode=explode, textprops={"fontsize": 16})
    plt.title(title, fontsize=20)

    plt.tight_layout()
    if save:
        plt.savefig(f"results/Figure_{graph_index}.png")
        graph_index += 1
    else:
        plt.show()


def plot_hist(data, title, xlabel, ylabel):
    global graph_index
    if not graph:
        return

    plt.figure(figsize=(12, 9))
    plt.hist(data, 25, edgecolor="black")
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    plt.tight_layout()
    if save:
        plt.savefig(f"results/Figure_{graph_index}.png")
        graph_index += 1
    else:
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

plot_pie(
    grade_dist,
    ["Prvý ročník", "Druhý ročník", "Tretí ročník", "Štvrtý ročník", "Piaty ročník"],
    "Distribúcia ročníkov",
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

plot_pie(sex_dist, ["Ženy", "Muži"], "Distribúcia pohlavia")

print("--- GPA ---")
print("n/a")
print("")

plot_hist(dataset[:, 2], "Distribúcia piemernu známok", "Piemerná známka", "Počet študent*iek")

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

plot_pie(math_dist, ["1", "2", "3", "4", "5"], "Distribúcia známok z matematiky")

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

plot_pie(slovak_dist, ["1", "2", "3", "4", "5"], "Distribúcia známok zo slovenčiny", (0, 0, 0, 0.25, 0.5))

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

plot_pie(english_dist, ["1", "2", "3", "4", "5"], "Distribúcia známok z angličtiny")

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

plot_pie(ses_dist, ["Nižšia trieda", "Stredná trieda", "Vyššia trieda"], "Distribúcia socio-ekonomických tried")

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

plot_pie(occupation_dist,
         ["Práca 10 a viac hodín týždenne", "Práca menej ako 10 hodín týždenne", "Šport", "Hudba", "Niečo iné",
          "Žiadne"], "Distribúcia práce a aktivít")

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

plot_pie(living_dist,
         ["S rodinou", "S rodinnou príslušní*čkou", "Sám*a alebo so spolubývajúc*ou", "Intrák", "Iné"],
         "Distribúcia životných situácií")

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

plot_pie(commute_dist,
         ["Intrák", "Menej ako 15 minút", "Menej ako 30 minút", "Menej ako hodinu", "Viac ako hodinu"],
         "Distribúcia dochádzania")

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

plot_pie(sleep_dist, ["6 hodín a menej", "7 až 8 hodín", "9 a viac hodín"], "Distribúcia spánku")

print("--- ABSENCE ---")
print("n/a")
print("")

plot_hist(dataset[:, 11], "Distribúcia absencií", "Počet neprítomných hodín", "Počet študent*iek")
