#from leagueleaders import LeagueLeaders2
from players.players import Players
import pandas as pd

df_leagueleaders = Players('Russell Wilson').get_data()

df_players = Players('D.K. Metcalf').get_data()

print(df_leagueleaders)
print(df_players)