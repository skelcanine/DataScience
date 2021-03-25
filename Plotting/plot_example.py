

import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-covid-data.csv', parse_dates=["date"], low_memory=False)

data = df[df.location.isin(['Germany', 'France', 'Italy', 'Spain']) ]
data = data[data['date'] > pd.Timestamp(2020, 4,1) ]


print(data)

fig = px.line(data, x="date", y="total_deaths", title='total_deaths in Germany', color='location')
fig.show()