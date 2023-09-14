from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests as re
import pandas as pd

class LeagueLeaders:
    def __init__(self, category, year):
        self.category = category
        self.year = year
        self.url = f'https://www.pro-football-reference.com/years/{year}/{category}.htm'

    def get_data(self):
        service = Service(ChromeDriverManager().install())
        option = Options()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.get(self.url)

        site = self.driver.page_source

        soup = BeautifulSoup(site, 'html.parser')

        #Obtendo tabela
        table = soup.find(
            'table',
            class_='per_match_toggle sortable stats_table now_sortable sticky_table eq2 re2 le2')

        #Cabeçalho
        thead = table.find(
            'thead'
            )
        
        headers = thead.find_all(
            'th'
        )

        cols = []

        for head in headers:
            cols.append(head.get_text())

        #Jogadores

        body = table.find(
            'tbody'
        )

        players = body.find_all(
            'tr'
        )

        data_list = []
        x = 0

        for player in players:
            data = player.find_all(
                'td'
            )
            player_data = []

            for stat in data:
                player_data.append(stat.get_text())       
            
            data_list.append(player_data)

        df = pd.DataFrame(data_list, columns=cols[1:])

        return df

        self.driver.quit() 

class LeagueLeaders2:
    def __init__(self, category, year):
        self.category = category.lower()
        self.year = year
        self.url = f'https://www.pro-football-reference.com/years/{self.year}/{self.category}.htm'

    def get_data(self):
        site = re.get(self.url)
        if str(site.status_code)[0] == '2':
            table = pd.read_html(self.url)[0]

            return table

            self.driver.quit()
        else:
            print("Dados não encontrados")


if __name__ == "__main__":
    league_leaders = LeagueLeaders('passing', '2023')



