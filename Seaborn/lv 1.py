import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set()

irisData = sns.load_dataset('iris')

print(irisData.head())

irisData.petal_length.plot()
irisData.plot()


# newPd = pd.Series(np.random.rand(7), index=list("ABCDEFG"))
#
# print(newPd)
# newPd.plot.bar(color='y', alpha=1)

plt.show()