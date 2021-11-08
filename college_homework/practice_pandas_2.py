# from pandas import read_csv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
# enqete = enqete.dropna()
# e = enqete
#
#
# age_graph = pd.cut(e['age'], labels=['20-30', '30-40', '41-50', '50+'], bins=[20, 30, 40, 50, np.inf])
# result = pd.crosstab(age_graph, e['diabetes'])
# result.plot(kind='bar', rot=0)
# print(result)
# plt.show()


# from pandas import read_csv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
# e = enqete
#
# age_graph = pd.cut(e['age'], labels=['20-30', '30-40', '41-50', '50+'], bins=[20, 30, 40, 50, np.inf])
# result = pd.crosstab(age_graph, e['diabetes'])
# result.plot(kind='bar', rot=0)
# print(result)
# plt.show()




from pandas import read_csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

enqete = read_csv("C:/Users/rad87/Documents/pima2.csv")
e = enqete

pregnant_graph = pd.cut(e['pregnant'],  labels=['0-5', '6-10', '10+'], bins=[-1, 5, 10, np.inf])
result = pd.crosstab(pregnant_graph, e['diabetes'])
result.plot(kind='bar', rot=0)
print(result)
plt.show()



# age_graph =  pd.cut(e['pregnant'], labels=['0-5', '6-10', '10+'], bins=[0, 5, 10, np.inf])
# result = pd.crosstab(age_graph, e['diabetes'])
# result.plot(kind='bar', rot=0)
# print(result)
# plt.show()
