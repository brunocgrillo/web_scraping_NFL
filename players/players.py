from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

class Players:
    def __init__(self, player_name, category='Regular Season'):
        self.player_name = player_name.strip()
        self.category = category
        self.first_name = self.player_name.split()[0]
        self.last_name = self.player_name.split()[1]
        self.url_name = re.sub(r'[^a-zA-Z0-9\s]', '', self.last_name)[:4] + re.sub(r'[^a-zA-Z0-9\s]', '', self.first_name)[:2]

    def get_data(self):
        url_final = ['00', '01', '02', '03', '99']
        self.url = f'https://www.pro-football-reference.com/players/{self.url_name[0]}/{self.url_name}{url_final[0]}.htm'
        site = requests.get(self.url)
        soup = BeautifulSoup(
            site.text,
            'html.parser')
        find_name= soup.find(
            'h1'
            )
        page_verify = find_name.get_text()
        print(self.url)
        if self.player_name != page_verify.strip():
            for x in url_final[1:]:
                self.url = f'https://www.pro-football-reference.com/players/{self.url_name[0]}/{self.url_name}{x}.htm'
                site = requests.get(self.url)
                soup = BeautifulSoup(
                site.text,
                'html.parser')
                find_name= soup.find(
                'h1'
                )
                page_verify = find_name.get_text()

                if self.player_name == page_verify.strip():
                    break
            if self.player_name != page_verify.strip():
                print('Jogador não encontrado')
            else:
                df = pd.read_html(self.url)[1]

                return df
        else:
            df = pd.read_html(self.url)[1]

            return df
if __name__ == '__main__':
    Players('Russel Wilson').get_data()