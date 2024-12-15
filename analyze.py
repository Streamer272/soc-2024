from typing import List

import numpy as np
import scipy.stats as stats


def analyze(name: str, data: List[np.ndarray]):
    F, p = stats.f_oneway(*data)
    print(f"F-stats for {name}: {F}")
    print(f"p-value for {name}: {p}")

    if p > 0.05:
        print("statistically insignificant\n")
        return

    print("statistically significant")
    tukey_results = stats.tukey_hsd(*data)
    print(tukey_results)
