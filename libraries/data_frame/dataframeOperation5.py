import pandas as pd


df = pd.read_csv('first.csv')
df2 = pd.read_csv('second.csv')


merge1=pd.merge(df, df2, left_on='id', right_on='id')
print(merge1)

merge2=pd.merge(df, df2, left_on='id', right_on='id', how='outer')
print(merge2)

merge3=pd.merge(df, df2, left_on='id', right_on='id', how='left')
print(merge3)

merge4=pd.merge(df, df2, left_on='id', right_on='id', how='right')
print(merge4)