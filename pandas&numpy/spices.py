import pandas as pd
import numpy as np

# displaing and elements then fill the NAN values by 5
data = pd.DataFrame(np.random.standard_normal((4, 3)))
print(data)
data.iloc[:2, 2] = np.nan
data.iloc[:1, 2] = np.nan
data.iloc[:4, 1] = np.nan
print(data)
print(data.fillna(5))

# displing the element of mhmd and mostafa and see is there's duplicate values
data1 = pd.DataFrame({"mhmd":["b", "a"]* 3, "mostafa": [1, 2, 5, 5, 5, 2]})
print(data1)
print(data1.duplicated())



