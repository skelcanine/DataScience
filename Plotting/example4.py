import pandas as pd
import numpy as np


import matplotlib.pyplot as plt

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=["date"], low_memory=False)

data = df[df.location.isin(['Germany', 'France', 'Italy', 'Spain'])]

data = data[(np.datetime64(pd.datetime.now().date()) - data['date']).astype('timedelta64[D]').astype(int) < 100 ].copy()

#data = data.groupby(["date","location"], as_index=False)['new_cases'].sum()

print(data)
plt.figure(figsize=(100, 10))
plt.subplot(1, 2, 1)
datax = data[data.location.isin(['Germany'])]
print(datax)
plt.plot(datax['date'], datax['new_cases'], c = "#FF914D", marker = "o", markersize = 10, linestyle = "-", linewidth = 3)
plt.show()