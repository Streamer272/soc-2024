import argparse
import numpy as np
import pandas as pd
import re

parser = argparse.ArgumentParser(
    prog="clean"
)
parser.add_argument("-i", "--input", required=True, help="Input dirty csv file")
parser.add_argument("-o", "--output", default="clean", help="Output clean csv file")
args = parser.parse_args()

# HEADERS: ["timestamp", "grade", "sex", "average grade", "math grade", "slovak grade", "english grade", "ses", "occupation", "living situation", "commute length", "sleep", "absence"]
df = pd.read_csv(args.input)
arr = df.to_numpy()
clean = []


# debugging purposes
# print(list([arr[i][12] for i in range(1, 20)]))
# exit(0)


def parse_gpa(txt: str) -> float:
    num_regex = r"\d+([,.]\d*)?"
    eu_num_regex = r"\d+(,\d*)?"

    txt = txt.strip()
    is_num = re.fullmatch(num_regex, txt) is not None
    if not is_num:
        print(f"ERROR: Couldn't parse gpa '{txt}'")
        ret = None
        while ret is None:
            fixed = input("Please enter fixed value: ")
            try:
                ret = float(fixed)
            except ValueError:
                pass
        return float(fixed)

    is_eu = re.fullmatch(eu_num_regex, txt) is not None
    if is_eu:
        txt = txt.replace(",", ".")

    return float(txt)


def parse_ses(txt: str) -> int:
    if txt.startswith("Nižšia trieda"):
        return 0
    elif txt.startswith("Stredná trieda"):
        return 1
    elif txt.startswith("Vyššia trieda"):
        return 2
    else:
        print("ERROR: Couldn't determine SES")
        return 3


def parse_occupation(txt: str) -> int:
    match txt:
        case "Pracujem 10 hodín a viac týždenne":
            return 0
        case "Pracujem menej ako 10 hodín týždenne":
            return 1
        case "Športujem na profesionálnej alebo polo-profesionálnej úrovni":
            return 2
        case "Robím muziku na profesionálnej alebo polo-profesionálnej úrovni":
            return 3
        case "Robím inú profesionálnu alebo polo-profesionálnu aktivitu":
            return 4
        case "Nie":
            return 5
        case _:
            print("ERROR: Couldn't determine occupation")
            return 6


def parse_living(txt: str) -> int:
    match txt:
        case "Bývam s rodičmi":
            return 0
        case "Bývam s iným rodinným príslušníkom/čkou":
            return 1
        case "Bývam sám alebo so spolubývajúcim/ou":
            return 2
        case "Bývam na intráku":
            return 3
        case "Mám to inak":
            return 4
        case _:
            print("ERROR: Couldn't determine living")
            return 5


def parse_commute(txt: str) -> int:
    match txt:
        case "Bývam na intráku":
            return 0
        case "Menej ako 15 minút":
            return 1
        case "Menej ako 30 minút":
            return 2
        case "Menej ako hodinu":
            return 3
        case "Viac ako hodinu":
            return 4
        case _:
            print("ERROR: Couldn't determine commute")
            return 5


def parse_sleep(txt: str) -> int:
    match txt:
        case "9 hodín a viac":
            return 0
        case "7 až 9 hodín":
            return 1
        case "6 hodín a menej":
            return 2
        case _:
            print("ERROR: Coudln't determine sleep")
            return 3


def parse_absence(txt: str) -> float:
    while True:
        try:
            return float(txt)
        except ValueError:
            print(f"ERROR: Couldn't parse absence '{txt}'")
            txt = input("Please enter fixed value: ")


for i in range(1, len(df)):
    row = arr[i]
    current = []

    grade = row[1]
    sex = row[2]
    gpa = row[3]
    math = row[4]
    slovak = row[5]
    english = row[6]
    ses = row[7]
    occupation = row[8]
    living = row[9]
    commute = row[10]
    sleep = row[11]
    absence = row[12]

    current.append(grade)
    current.append(0 if sex == "Žena" else 1)  # zena = 0, muz = 1
    current.append(parse_gpa(gpa))
    current.append(math)
    current.append(slovak)
    current.append(english)
    current.append(parse_ses(ses))
    current.append(parse_occupation(occupation))
    current.append(parse_living(living))
    current.append(parse_commute(commute))
    current.append(parse_sleep(sleep))
    current.append(parse_absence(absence))

    clean.append(np.array(current))

print(f"Saving {len(arr)} rows")
np.save(args.output, np.array(clean))
