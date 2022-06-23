from mcc import MCC
import plotly.express as px
import pandas as pd

mc = MCC()

stats = pd.read_csv("out.csv")
print(stats)

fig = px.bar(
    stats,
    x="Color",
    y="Coins",
    text="Username",
    color="Color",
    color_discrete_sequence=["#fc2003", "#ff7105", "#fcd703", "#73ff00", "#167d1a", "#00fff7", "#1e81a8", "#1111cf", "#6e19cf", "#ff3de2"]
)
fig.show()