import pandas as pd


df = pd.read_csv('train.csv')

print(df.groupby(["Sex","Pclass"],as_index=False)["Age"].mean())


print(df.groupby(by="Embarked").sum())
