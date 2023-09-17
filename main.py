from leagueleaders import LeagueLeaders, LeagueLeaders2
from players import Players
import pandas as pd

df_leagueleaders = LeagueLeaders2('passing', '2022').get_json()

df_players = Players('Russell Wilson').get_json()

print(df_leagueleaders)
print(df_players)