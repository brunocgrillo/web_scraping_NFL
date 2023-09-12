from leagueleaders import LeagueLeaders
from players import Players
import pandas as pd

df = Players('Russell Wilson').get_data()

print(df)