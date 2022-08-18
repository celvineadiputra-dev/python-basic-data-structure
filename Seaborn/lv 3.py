import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# newData = np.random.rand(6, 8)
# heatMap = sns.heatmap(newData)
# plt.show()


tipsData = sns.load_dataset('tips')
print(tipsData.head())
tipDataNew = pd.crosstab(tipsData["day"], tipsData["size"])
tipsHeatMap = sns.heatmap(tipDataNew)


# irisData = sns.load_dataset('iris')
# print(irisData.head())
# irisDataNew = pd.crosstab(irisData['species'], irisData['petal_length'])
# irisHetMap = sns.heatmap(irisDataNew)

plt.show()
