import pandas as pd

series = pd.Series([10, 20, 10, 100])
print(series)
print(type(series))

series_index = pd.Series([10, 1, 2, 5], index=["a", "b", "c", "d"])
print(series_index)

colors = ["Blue", "Dark Blue", "Sky Blue"]
degrees = [40, 10, 50]

dataFrame = pd.DataFrame({
    "colors": colors,
    "degrees": degrees,
}, columns=["colors", "degrees"], index=range(1, 4))

print(dataFrame)