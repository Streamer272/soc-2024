import argparse
import numpy as np

parser = argparse.ArgumentParser(
    prog="print"
)
parser.add_argument("-i", "--input", default="clean.npy", help="Input npy file")
args = parser.parse_args()

arr = np.load(args.input, allow_pickle=False)
print(arr)
