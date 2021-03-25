import pandas as pd


df = pd.read_csv('train.csv')
df2 = pd.read_csv('test.csv')

all_data = pd.concat([df,df2])
print(len(all_data))