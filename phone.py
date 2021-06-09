import csv
import pandas as pd
import plotly.figure_factory as ff
#read the file
df=pd.read_csv("data.csv")
mobile=df["Avg Rating"].tolist()

fig=ff.create_distplot([mobile],["Average Rating of Mobile Phones"])
fig.show()