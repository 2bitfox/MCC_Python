import requests

class MCC:
    def __init__(self):
        self.game = {
            "Rocket Spleef": "MG_ROCKET_SPLEEF",
            "Survival Games": "MG_SURVIVAL_GAMES",
            "Parkour Warrior": "MG_PARKOUR_WARRIOR",
            "Ace Race": "MG_ACE_RACE",
            "Bingo but Fast": "MG_BINGO_BUT_FAST",
            "TGTTOS": "MG_TGTTOSAWAF",
            "Skyblockle": "MG_SKYBLOCKLE",
            "Sky Battle": "MG_SKY_BATTLE",
            "Hole in the Wall": "MG_HOLE_IN_THE_WALL",
            "Battle Box": "MG_BATTLE_BOX",
            "Buildmart": "MG_BUILD_MART",
            "Sands of Time": "MG_SANDS_OF_TIME",
            "Dodgebolt": "MG_DODGEBOLT",
            "Parkour Tag": "MG_PARKOUR_TAG",
            "Grid Runners": "MG_GRID_RUNNERS",
            "Meltdown": "MG_MELTDOWN",
            "Global Statistics": "GLOBAL_STATISTICS",
            "Legacy Statistics": "LEGACY_STATISTICS"
        }

        self.team = {
            "Red":"RED",
            "Orange":"ORANGE",
            "Yellow":"YELLOW",
            "Lime":"LIME",
            "Green":"GREEN",
            "Aqua":"AQUA",
            "Cyan":"CYAN",
            "Blue":"BLUE",
            "Purple":"PURPLE",
            "Pink":"PINK",
            "Spectators":"SPECTATORS",
            "None":"NONE"
        }


    def event(self):
        api_url = "https://api.mcchampionship.com/v1/event"
        response = requests.get(api_url)

        return response
    
    def hof(self):
        api_url="https://api.mcchampionship.com/v1/halloffame/"
        response = requests.get(api_url)

        return response

    def hof_event(self, event):

        if event in self.game:
            api_url="https://api.mcchampionship.com/v1/halloffame/" + self.game.get(event)
            response = requests.get(api_url)

            return response
        else:
            return("That is not a valid mcc game")

    def rundown(self):
        api_url = "https://api.mcchampionship.com/v1/rundown"
        response = requests.get(api_url)

        return response

    def participants(self):
        api_url = "https://api.mcchampionship.com/v1/participants"
        response = requests.get(api_url)

        return response
    
    def teams(self, team):

        if team in self.team:
            api_url = "https://api.mcchampionship.com/v1/participants/" + self.team.get(team)
            response = requests.get(api_url)

            return response
        else:
            return("That is not a valid team")
