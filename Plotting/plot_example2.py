
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-covid-data.csv', parse_dates=["date"], low_memory=False)

data = df.groupby('continent', as_index=False).mean()

fig = px.bar(data_frame=data,
             x='continent',
             y='new_deaths',color='new_deaths')
fig.show()