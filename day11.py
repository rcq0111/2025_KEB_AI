import pandas as pd

df =pd.DataFrame(
    [[4, 7 ,10],
         [5, 88 ,11],
         [16, 9 ,12]],
         index=(1, 2, 3),
         columns=('a', 'b', 'c')
)
print(df)

#df3 = df.iloc[0:2]
#df3 =df.loc[1:2]
df3 = df.iloc[:, [0,2]]
print(len(df3))

# df2 = pd.melt(df).rename(columns={'variable' : 'var', 'value' : 'val'}).query('val >= 10').sort_values('val', ascending=False)
#
# print(df2)