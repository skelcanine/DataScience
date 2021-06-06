import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('owid-covid-data.csv', parse_dates=["date"], low_memory=False)
data = df[df.location.isin(['Germany'])]

data = data[['date', 'total_cases']].set_index('date')

plt.figure(figsize=(25, 10))

print(data)

plt.subplot(3,1,1)

plt.hist(data['total_cases'], color="#FF914D", bins=len(data))
plt.show()