import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=["date"], low_memory=False)

data = df.groupby('location', as_index=False)["total_cases"].max().sort_values(by=['total_cases'], ascending=False).head(20)
print(data)



plt.bar(x = data['location'], height = ['total_cases'], color = "#22B573")
plt.xlabel('Countries')
plt.ylabel('Total Cases')

plt.show()