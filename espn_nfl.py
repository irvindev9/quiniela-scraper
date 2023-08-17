#!/usr/bin/env python3

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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

response = requests.get(f'https://www.espn.com.mx/futbol-americano/nfl/resultados/_/semana/{sys.argv[1]}/ano/{sys.argv[2]}/tipodetemporada/2', headers=headers)

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