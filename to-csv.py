import numpy as np
import pandas as pd

arr = np.load("clean.npy")
df = pd.DataFrame(arr)
df.columns = ["grade", "sex", "average grade", "math grade", "slovak grade", "english grade", "ses", "occupation", "living situation", "commute length", "sleep", "absence"]
df.to_csv("clean.csv")
