import pandas as pd

sample = pd.read_csv("../Sample/sample1.csv", low_memory=False)
print(sample)
print(sample.info())
print(sample.describe())
print(sample.loc[sample["price"].argmax()][["Cars", "price"]])
print(sample.loc[sample["price"].argmin()][["Cars", "price"]])