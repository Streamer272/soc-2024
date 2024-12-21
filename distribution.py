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
    plt.bar(["Prvý ročník", "Druhý ročník", "Tretí ročník", "Štvrtý ročník", "Piaty ročník"],
            np.array(grade_dist) * 100)
    plt.ylim(0, 100)
    for i in range(5):
        plt.text(i - 0.25, grade_dist[i] * 100 + 1, percent(grade_dist[i]))
    plt.title("Distribúcia ročníkov")
    plt.xlabel("Ročník")
    plt.ylabel("Percentá")
    plt.show()

exit(0)

sex = dataset[:, 1]
print("--- SEX ---")
print(f"Female: {percent(len(sex[sex == 0]), len(sex))}")
print(f"Male: {percent(len(sex[sex == 1]), len(sex))}")
print("")

print("--- GPA ---")
print("n/a")
print("")

math = dataset[:, 3]
print("--- MATH ---")
print(f"1: {percent(len(math[math == 1]), len(math))}")
print(f"2: {percent(len(math[math == 2]), len(math))}")
print(f"3: {percent(len(math[math == 3]), len(math))}")
print(f"4: {percent(len(math[math == 4]), len(math))}")
print(f"5: {percent(len(math[math == 5]), len(math))}")
print("")

slovak = dataset[:, 4]
print("--- SLOVAK ---")
print(f"1: {percent(len(slovak[slovak == 1]), len(slovak))}")
print(f"2: {percent(len(slovak[slovak == 2]), len(slovak))}")
print(f"3: {percent(len(slovak[slovak == 3]), len(slovak))}")
print(f"4: {percent(len(slovak[slovak == 4]), len(slovak))}")
print(f"5: {percent(len(slovak[slovak == 5]), len(slovak))}")
print("")

english = dataset[:, 5]
print("--- ENGLISH ---")
print(f"1: {percent(len(english[english == 1]), len(english))}")
print(f"2: {percent(len(english[english == 2]), len(english))}")
print(f"3: {percent(len(english[english == 3]), len(english))}")
print(f"4: {percent(len(english[english == 4]), len(english))}")
print(f"5: {percent(len(english[english == 5]), len(english))}")
print("")

ses = dataset[:, 6]
print("--- SES ---")
print(f"Lower: {percent(len(ses[ses == 0]), len(ses))}")
print(f"Middle: {percent(len(ses[ses == 1]), len(ses))}")
print(f"Upper: {percent(len(ses[ses == 2]), len(ses))}")
print("")

occupation = dataset[:, 7]
print("--- OCCUPATION ---")
print(f"work hours / week >= 10: {percent(len(occupation[occupation == 0]), len(occupation))}")
print(f"work hours / week < 10 : {percent(len(occupation[occupation == 1]), len(occupation))}")
print(f"sport                  : {percent(len(occupation[occupation == 2]), len(occupation))}")
print(f"music                  : {percent(len(occupation[occupation == 3]), len(occupation))}")
print(f"other                  : {percent(len(occupation[occupation == 4]), len(occupation))}")
print(f"none                   : {percent(len(occupation[occupation == 5]), len(occupation))}")
print("")

living = dataset[:, 8]
print("--- LIVING ---")
print(f"with family       : {percent(len(living[living == 0]), len(living))}")
print(f"with family member: {percent(len(living[living == 1]), len(living))}")
print(f"alone / roomates  : {percent(len(living[living == 2]), len(living))}")
print(f"dorms             : {percent(len(living[living == 3]), len(living))}")
print(f"other             : {percent(len(living[living == 4]), len(living))}")
print("")

commute = dataset[:, 9]
print("--- COMMUTE ---")
print(f"dorms : {percent(len(commute[commute == 0]), len(commute))}")
print(f"<= 15m: {percent(len(commute[commute == 1]), len(commute))}")
print(f"<= 30m: {percent(len(commute[commute == 2]), len(commute))}")
print(f"<= 1h : {percent(len(commute[commute == 3]), len(commute))}")
print(f"> 1h  : {percent(len(commute[commute == 4]), len(commute))}")
print("")

sleep = dataset[:, 10]
print("--- SLEEP ---")
print(f"short sleepers : {percent(len(sleep[sleep == 0]), len(sleep))}")
print(f"medium sleepers: {percent(len(sleep[sleep == 1]), len(sleep))}")
print(f"long sleepers  : {percent(len(sleep[sleep == 2]), len(sleep))}")
print("")

print("--- ABSENCE ---")
print("n/a")
print("")
