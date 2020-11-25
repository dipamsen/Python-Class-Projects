# Data Visualization
import pandas as pd
import plotly_express as px

scatter_data = pd.read_csv("D://Documents/Pythony Stuff/dataviz/data.csv")

scatter_chart = px.scatter(scatter_data, x="InternetUsers",
                           y="Population", color="Country")

scatter_chart.show()
