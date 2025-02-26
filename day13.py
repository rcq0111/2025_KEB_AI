import pandas as pd

data = [1, 7, 5, 2, 8, 3, 6, 4]

bins = [0, 3, 6, 9]

lables = ["low", "mid", "high"]

cat = pd.cut(data, bins, False, lables) # right는 0, 3, 6, 9 포함 미포함
print(cat)