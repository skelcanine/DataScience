



import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-covid-data.csv', parse_dates=["date"], low_memory=False)
data = df[df.location.isin(['Germany'])]


print(data)
fig = px.histogram(data, x="date", y="new_deaths", nbins=365)
fig.show()