import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
tipsData = sns.load_dataset('tips')

print(tipsData.head())

sizeOfDay = pd.crosstab(tipsData["day"], tipsData["size"])

print(sizeOfDay)

sizeOfDay.plot.barh()
sizeOfDay.plot.bar()
sizeOfDay.plot.hist()

plt.show()