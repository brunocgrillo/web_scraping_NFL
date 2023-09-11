from leagueleaders import LeagueLeaders
import pandas as pd

print('Category (passing/rushing/receiving)')
category = input()
print('Year (1970-2023)')
year = input()
df = LeagueLeaders(category, year).get_data()

print(df)

