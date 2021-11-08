from pandas import read_csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
e = enqete

# pregnant_graph = cut 함수 사용
# barplot
result = pd.crosstab(pregnant_graph, e['diabetes'])
result.plot(kind='bar', rot=0)
print(result)
plt.show()