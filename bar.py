import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
print(df.head())
df.head()
fig = px.bar(df, x = "Country", y = "InternetUsers", color = "Country", title = "InternetUsers")
fig.show()