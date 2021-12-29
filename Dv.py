import pandas as pd
import plotly.express as px

dv = pd.read_csv("Data.csv")
fig = px.scatter(dv,x="date",y="cases",color="country",size_max=20,title="Covid Cases records")

fig.show()