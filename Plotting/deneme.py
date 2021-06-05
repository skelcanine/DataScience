import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=["date"], low_memory=False)


data = df.groupby('continent',as_index=False )['total_deaths'].mean()
print(data)

plt.figure(figsize=(12, 3), dpi = 500)
sns.barplot(x = 'continent', y = 'total_deaths', data = data, ci = 'sd')
plt.xticks(rotation = 90)
plt.show()