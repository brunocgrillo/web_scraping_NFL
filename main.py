import requests as re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import json

url = 'https://www.nfl.com/stats/player-stats/category/passing/2022/REG/all/passingyards/DESC'

service = Service(ChromeDriverManager().install())
option = Options()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

driver.get(url)

site = driver.page_source

soup = BeautifulSoup(site, 'html.parser')

#Obtendo tabela
table = soup.find(
    'table',
    class_='d3-o-table d3-o-table--detailed d3-o-player-stats--detailed d3-o-table--sortable')

#Cabeçalho
headers = table.find_all(
    'th',
    class_='header')

header = []

for head in headers:
    header.append(head.get_text().replace('\n', ''))

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
        player_data.append(stat.get_text().replace('\n', '').replace(' ', ''))       
    
    data_list.append(player_data)

df = pd.DataFrame(data_list, columns=header)

print(df)

