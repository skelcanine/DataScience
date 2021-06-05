import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=["date"], low_memory=False)
data = df[df.location.isin(['Germany'])]

data = data[['date','new_deaths','new_cases']]

print(data)
print(data['new_cases'].max())

fig = plt.figure(figsize=(35, 10))
ax1 = fig.add_subplot(111)

plt.scatter(data.date, data.new_cases, s=10, c='b', marker="s", label='New Cases')
#plt.scatter(df['date'],df['new_deaths'], s=2, c='r', marker="o", label='New Deaths')
plt.legend(loc='upper left');
plt.show()

