from pandas import read_csv
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import pylab as pl

mat.rcParams['font.family'] = 'Malgun Gothic'
enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
enqete = enqete.dropna()
e = enqete
diabetes = ["neg", "pos"]
results = []

def percentile_25(x):
    return x.quantile(0.25)
def percentile_75(x):
    return x.quantile(0.75)


for c in diabetes:
    condition = e.diabetes == c
    df = e[condition].loc[:, ["glucose", "pressure", "triceps", "insulin", "mass", "pedigree", "age"]]
    result = df.agg(
        {
            "glucose": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "pressure": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "triceps": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "insulin": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "mass": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "pedigree": ["min", "max", "median", "mean", percentile_25, percentile_75],
            "age": ["min", "max", "median", "mean", percentile_25, percentile_75],

        }
    )
    results.append(result)

for name, data in zip(diabetes, results):
    print(name)
    # output
    print(data, "\n")

    #histogram
    data.hist(grid=False)
    plt.subplots_adjust(hspace=0.5)
    pl.suptitle(f"{name}")
    plt.show()

#boxplot
fig = plt.subplots(figsize=(16, 7))
ax = [
    plt.subplot(121),
    plt.subplot(122)]
results[0].boxplot(grid=False, ax=ax[0])
results[1].boxplot(grid=False, ax=ax[1])
ax[0].set_ylabel('val', fontsize='12')
ax[1].set_ylabel('val', fontsize='12')
ax[0].set_title('neg')
