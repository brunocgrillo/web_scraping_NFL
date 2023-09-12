from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import requests as re

class Players:
    def __init__(self, player_name, category='Regular Season'):
        self.player_name = player_name.strip()
        self.category = category
        self.first_name = self.player_name.split()[0]
        self.last_name = self.player_name.split()[1]
        self.url_name = self.last_name[:4] + self.first_name[:2]

    def get_data(self):
        url_final = ['00', '01', '02', '03', '99']
        self.url = f'https://www.pro-football-reference.com/players/{self.url_name[0]}/{self.url_name}{url_final[0]}.htm'
        service = Service(ChromeDriverManager().install())
        option = Options()
        self.driver = webdriver.Chrome(service=service, options=option)
        
        site = re.get(self.url)
        print(site.status_code)
        soup = BeautifulSoup(
            site.text,
            'html.parser')
        find_name= soup.find(
            'h1'
            )
        page_verify = find_name.get_text()
        print(f"[{self.player_name}] == [{page_verify}]")
        print(self.player_name == page_verify.strip())
        print(self.url)
        print(f'{self.player_name} {page_verify}')

        if self.player_name != page_verify.strip():
            for x in url_final[1:]:
                self.url = f'https://www.pro-football-reference.com/players/{self.url_name[0]}/{self.url_name}{x}.htm'
                self.driver.get(self.url)
                site = self.driver.page_source
                soup = BeautifulSoup(
                site,
                'html.parser')
                find_name= soup.find(
                'h1'
                )
                page_verify = find_name.get_text()

                if page_verify.strip() == self.player_name:
                    break
        
        df = pd.read_html(self.url)[0]

        return df

if __name__ == '__main__':
    Players('Russel Wilson').get_data()