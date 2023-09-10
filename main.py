from leagueleaders import LeagueLeaders
import pandas as pd

df = LeagueLeaders('rushing', '2022').get_data()

print(df)

