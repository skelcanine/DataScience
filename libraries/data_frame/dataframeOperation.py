import pandas as pd


df = pd.read_csv('train.csv')
#my_list = df.columns.values.tolist()
edited_df = df[df['Age']>30]
calclist= list(edited_df['Survived'].value_counts())
print(edited_df['Survived'].value_counts())
survival_rate = calclist[1]/(calclist[0]+calclist[1])
print("Survival rate= %", survival_rate*100)