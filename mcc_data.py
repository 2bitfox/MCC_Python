from mcc import MCC
import plotly.express as px
import pandas as pd

#new instance of the api
mc = MCC()

# get rundown of the event from the api
rd = mc.rundown()
player_points = rd.json()["data"]["individualScores"]

# get yellow team from the api
yellow_team = mc.teams("Yellow").json()
yellow_names = []

# grab the usernames of everyone on yellow team
x = 0
while x < 4:
    name = yellow_team["data"][x]["username"]
    yellow_names.append(name)
    x += 1

print (yellow_names)

# grab their points
scores = []
for i in yellow_names:
    scores.append(player_points[i])

print(scores)

# example plot. probably a better way to display this but this is just to show an example
yellow = pd.DataFrame(
    {
        "Username":yellow_names,
        "Coins": scores
    }
)

print(yellow)

plot = px.histogram(yellow, x="Username", y="Coins")
plot.show()