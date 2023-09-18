import requests
import pandas as pd
import json
import datetime

class TeamGameLogs:
    def __init__(self, team, year):
        self.team = team.strip().lower()
        self.year = str(year).strip()
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
            date_year = datetime.datetime.now()
            if self.year == date_year.year:
                table = pd.read_html(self.url)[2]
                table.columns = table.columns.droplevel(0) + "_" + table.columns.get_level_values(0)
                table.columns = table.columns.str.split('_U').str[0]
                return table
            else:
                table = pd.read_html(self.url)[1]
                table.columns = table.columns.droplevel(0) + "_" + table.columns.get_level_values(0)
                table.columns = table.columns.str.split('_U').str[0]
                return table

    def get_json(self):
        site = requests.get(self.url)
        if str(site.status_code)[0] != '2':
            print('Problema na coleta de dados')
            return
        else:
            date_year = datetime.datetime.now()
            if self.year == date_year.year:
                table = pd.read_html(self.url)[2]
                table.columns = table.columns.droplevel(0) + "_" + table.columns.get_level_values(0)
                table.columns = table.columns.str.split('_U').str[0]
                data_dict = table.to_dict(orient='records')
                return json.dumps(data_dict, indent=1)
            else:
                table = pd.read_html(self.url)[1]
                table.columns = table.columns.droplevel(0) + "_" + table.columns.get_level_values(0)
                table.columns = table.columns.str.split('_U').str[0]
                data_dict = table.to_dict(orient='records')
                return json.dumps(data_dict, indent=1)
