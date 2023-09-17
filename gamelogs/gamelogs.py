import requests
import pandas as pd
import json

class TeamGameLogs:
    def __init__(self, team, year):
        self.team = team.strip().lower()
        self.year = year.strip()
        teams = ['cardinals', 'falcons', 'ravens', 'bills', 'panthers', 'bears', 'bengals', 'browns', 'cowboys',
                      'broncos', 'lions', 'texans', 'packers', 'colts', 'jaguars', 'chiefs', 'raiders', 'chargers', 'rams',
                      'dolphins', 'vikings', 'patriots', 'saints', 'giants', 'jets', 'eagles', 'steelers', '49ers', 'seahawks',
                      'buccaneers', 'titans', 'commanders']
        team_tags = ['crd', 'atl', 'rav', 'buf', 'car', 'chi', 'cin', 'cle', 'dal', 'den', 'det', 'gnb', 'htx', 'clt', 'jax',
                     'kan', 'rai', 'sdg', 'ram', 'mia', 'min', 'nwe', 'nor', 'nyg', 'nyj', 'phi', 'pit', 'sfo', 'sea', 'tam', 'oti', 'was']
        dictionary = dict(zip(teams, team_tags))

        try:
            self.tag = dictionary[self.team]
        except:
            print('Time não encontrado')
            self.tag = None

        self.url = f'https://www.pro-football-reference.com/teams/{self.tag}/{self.year}.htm'

    def get_dataframe(self):
        site = requests.get(self.url)
        if str(site.status_code)[0] != '2':
            print('Problema na coleta de dados')
            return
        else:
            table = pd.read_html(self.url)[1]
            return table

    def get_json(self):
        site = requests.get(self.url)
        if str(site.status_code)[0] != '2':
            print('Problema na coleta de dados')
            return
        else:
            table = pd.read_html(self.url)[1]
            data_dict = table.to_dict(orient='records')
            new_data_dict = [dict(((key[1], value) for key, value in data.items())) for data in data_dict]
            return json.dumps(new_data_dict, indent=1)
