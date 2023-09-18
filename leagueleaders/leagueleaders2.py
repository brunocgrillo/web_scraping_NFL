import requests
import pandas as pd
import json

class LeagueLeaders2:
    def __init__(self, category, year):
        self.category = category.lower()
        self.year = str(year).strip()
        self.url = f'https://www.pro-football-reference.com/years/{self.year}/{self.category}.htm'

    def get_dataframe(self):
        site = requests.get(self.url)
        if str(site.status_code)[0] == '2':
            df = pd.read_html(self.url)[0]
            df.replace(['\*', '\+'], '', regex=True, inplace=True)

            return df
        else:
            print("Dados não encontrados")

    def get_json(self):
        site = requests.get(self.url)
        if str(site.status_code)[0] == '2':
            df = pd.read_html(self.url)[0]
            df.replace(['\*', '\+'], '', regex=True, inplace=True)

            data_dict = df.to_dict(orient='records')
            
            return json.dumps(data_dict, indent=1)
        else:
            print("Dados não encontrados")
            return None

if __name__ == "__main__":
    league_leaders = LeagueLeaders2('passing', '2023')