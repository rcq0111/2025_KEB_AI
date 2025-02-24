import pandas as pd

df =pd.DataFrame(
    [[4, 7 ,10],
         [5, 88 ,11],
         [16, 9 ,12]],
         index=(1, 2, 3),
         columns=('a', 'b', 'c')
)
print(df)

df2 = pd.melt(df).rename(columns={'variable' : 'var', 'value' : 'val'}).query('val >= 10')
print(df2)