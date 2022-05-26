from bs4 import BeautifulSoup
import requests
import sys

# Verify that user enter the correct number of arguments
if len(sys.argv) < 3:
    print("Usage: espn_nfl.py <week> <year>")
    sys.exit(1)

# parse the arguments
sys.argv[1] = int(sys.argv[1])
sys.argv[2] = int(sys.argv[2])

# sys.argv[1] is integer week
if type(sys.argv[1]) != int:
    print("Invalid week")
    sys.exit(1)

# sys.argv[2] is integer year
if type(sys.argv[2]) != int:
    print("Invalid year")
    sys.exit(1)

response = requests.get(f'https://www.espn.com.mx/futbol-americano/nfl/resultados/_/semana/{sys.argv[1]}/ano/{sys.argv[2]}/tipodetemporada/2')

scoreboard = BeautifulSoup(response.text, "html.parser")

games = scoreboard.find_all("section", class_="Scoreboard")

save_games = []

for game in games:
  team = game.find_all("li", class_="ScoreboardScoreCell__Item")

  team1 = team[0].find("div", class_="ScoreCell__TeamName").text
  team2 = team[1].find("div", class_="ScoreCell__TeamName").text

  save_game = {
    "team1": team1,
    "team2": team2
  }

  save_games.append(save_game)

print(save_games)