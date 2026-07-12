# mhmd amin

import pandas as pd
import numpy as np

# create simple series object
data1 = pd.Series(np.arange(5), index=["A", "B", "C", "D", "E"])
var = data1.index.is_unique
print(data1)
print(var)

# create simple data frame
data = {"state": ["cairo", "athena", "port"],
        "year": [2000, 2001, 2002],
        "pop": ["2m", "5m", "1.5m"]}

frame = pd.DataFrame(data)
print(data)
