
from pandas import read_csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
e = enqete
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pregnant_graph = pd.cut(e['pregnant'],  labels=['0-5', '6-10', '10+'], bins=[-1, 5, 10, np.inf])

ff = pd.merge(e.reset_index(), pregnant_graph.reset_index(), on='index')
result = ff.groupby(["diabetes", "pregnant_y"])
result = result.agg(
    {
# agg의 사용법을 적용시키는 공간
    }
)
print(result)
