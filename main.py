from leagueleaders import LeagueLeaders, LeagueLeaders2
from players import Players
import pandas as pd

df_leagueleaders = LeagueLeaders2('PaSSing', '2022').get_data()

df_players = Players('Jamal Adams').get_data()

print(df_leagueleaders)
print(df_players)