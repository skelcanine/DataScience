import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-covid-data.csv', parse_dates=["date"], low_memory=False)

data = df.groupby('continent', as_index=False)["total_deaths"].max()
data["total_deaths"] = data["total_deaths"].div(365)
print(data)

