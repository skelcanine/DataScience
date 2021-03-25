import pandas as pd


df = pd.read_csv('train.csv')

print("Average of female age",df.groupby("Sex")["Age"].mean()[0])
print("Average of male age",df.groupby("Sex")["Age"].mean()[1])

print(df.groupby(by="Embarked").sum())
