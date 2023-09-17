from gamelogs.gamelogs import TeamGameLogs

df = TeamGameLogs('Cardinals', '2022').get_json()

print(df)