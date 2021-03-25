import pandas as pd


df = pd.read_csv('train.csv')

edited_df_male = df[df['Sex'] == "male"]
edited_df_female = df[df['Sex'] == "female"]

calclist= list(edited_df_female['Survived'].value_counts())
survival_rate = calclist[1]/(calclist[0]+calclist[1])
print("Survival rate of females= %", survival_rate*100)

calclist= list(edited_df_male['Survived'].value_counts())
survival_rate = calclist[1]/(calclist[0]+calclist[1])
print("Survival rate of males= %", survival_rate*100)