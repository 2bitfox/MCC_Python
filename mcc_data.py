from mcc import MCC
import plotly.express as px
import pandas as pd

#new instance of the api
mc = MCC()

# get rundown of the event from the api
rd = mc.rundown()
player_points = rd.json()["data"]["individualScores"]

# pull team data

red_team = mc.teams("Red").json()
red_names = []

orange_team = mc.teams("Orange").json()
orange_names = []

yellow_team = mc.teams("Yellow").json()
yellow_names = []

lime_team = mc.teams("Lime").json()
lime_names = []

green_team = mc.teams("Green").json()
green_names = []

aqua_team = mc.teams("Aqua").json()
aqua_names = []

cyan_team = mc.teams("Cyan").json()
cyan_names = []

blue_team = mc.teams("Blue").json()
blue_names = []

purple_team = mc.teams("Purple").json()
purple_names = []

pink_team = mc.teams("Pink").json()
pink_names = []


# grab the usernames of everyone

x = 0
while x < 4:
    name = red_team["data"][x]["username"]
    red_names.append(name)

    name = orange_team["data"][x]["username"]
    orange_names.append(name)

    name = yellow_team["data"][x]["username"]
    yellow_names.append(name)

    name = lime_team["data"][x]["username"]
    lime_names.append(name)

    name = green_team["data"][x]["username"]
    green_names.append(name)

    name = aqua_team["data"][x]["username"]
    aqua_names.append(name)

    name = cyan_team["data"][x]["username"]
    cyan_names.append(name)

    name = blue_team["data"][x]["username"]
    blue_names.append(name)

    name = purple_team["data"][x]["username"]
    purple_names.append(name)

    name = pink_team["data"][x]["username"]
    pink_names.append(name)

    x += 1

# grab scores

rscores = []
for i in red_names:
    rscores.append(player_points[i])

oscores = []
for i in orange_names:
    oscores.append(player_points[i])

yscores = []
for i in yellow_names:
    yscores.append(player_points[i])

lscores = []
for i in lime_names:
    lscores.append(player_points[i])

gscores = []
for i in green_names:
    gscores.append(player_points[i])

ascores = []
for i in aqua_names:
    ascores.append(player_points[i])

cscores = []
for i in cyan_names:
    cscores.append(player_points[i])

bscores = []
for i in blue_names:
    bscores.append(player_points[i])

pscores = []
for i in purple_names:
    pscores.append(player_points[i])

piscores = []
for i in pink_names:
    piscores.append(player_points[i])

# turn the data into a dataframe
teams = pd.DataFrame(
    {
        "Username": red_names,
        "Coins": rscores,
        "Color": "Red"
    }
)

oteam = pd.DataFrame(
    {
        "Username": orange_names,
        "Coins": oscores,
        "Color": "Orange"
    }
)

yteam = pd.DataFrame(
    {
        "Username": yellow_names,
        "Coins": yscores,
        "Color": "Yellow"
    }
)


lteam = pd.DataFrame(
    {
        "Username": lime_names,
        "Coins": lscores,
        "Color": "Lime"
    }
)

gteam = pd.DataFrame(
    {
        "Username": green_names,
        "Coins": gscores,
        "Color": "Green"
    }
)

ateam = pd.DataFrame(
    {
        "Username": aqua_names,
        "Coins": ascores,
        "Color": "Aqua"
    }
)

cteam = pd.DataFrame(
    {
        "Username": cyan_names,
        "Coins": cscores,
        "Color": "Cyan"
    }
)

bteam = pd.DataFrame(
    {
        "Username":blue_names,
        "Coins": bscores,
        "Color": "Blue"
    }
)

pteam = pd.DataFrame(
    {
        "Username": purple_names,
        "Coins": pscores,
        "Color": "Purple"
    }
)

piteam = pd.DataFrame(
    {
        "Username": pink_names,
        "Coins": piscores,
        "Color": "Pink"
    }
)

teams = teams.append([oteam, yteam, lteam, gteam, ateam, cteam, bteam, pteam, piteam])

teams.to_csv("out.csv")
print(teams)

plot = px.histogram(teams, x="Color", y="Coins", color="Username")
plot.show()
