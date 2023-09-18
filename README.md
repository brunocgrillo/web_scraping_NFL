# Projeto de Web Scraping Pro-Football-Focus

Este projeto permite extrair dados do site Pro-Football-Focus relacionados a jogadores, líderes da liga e logs de jogos de times. Ele é composto por quatro módulos: LeagueLeaders, LeagueLeaders2, Players e TeamGameLogs.

## Módulo LeagueLeaders

### Descrição
O módulo `LeagueLeaders` é responsável por extrair os líderes da liga em uma categoria específica para um ano determinado. Ele utiliza as bibliotecas Selenium, web_driver_manager e BeautifulSoup para realizar o scraping.

### Parâmetros
- `categoria` (str): A categoria desejada para a extração (opções disponíveis: passing, running, receiving, kicking).
- `ano` (int): O ano para o qual deseja extrair os dados.

### Métodos
- `get_dataframe()`: Retorna os dados em um DataFrame.
- `get_json()`: Retorna os dados em formato JSON.

## Módulo LeagueLeaders2

### Descrição
O módulo `LeagueLeaders2` é semelhante ao `LeagueLeaders`, mas oferece uma alternativa que utiliza as bibliotecas requests e pandas para extrair os líderes da liga em uma categoria específica para um ano determinado.

### Parâmetros
- `categoria` (str): A categoria desejada para a extração (opções disponíveis: passing, running, receiving, kicking).
- `ano` (int): O ano para o qual deseja extrair os dados.

### Métodos
- `get_dataframe()`: Retorna os dados em um DataFrame.
- `get_json()`: Retorna os dados em formato JSON.

## Módulo Players

### Descrição
O módulo `Players` permite extrair dados de um jogador específico. Você pode escolher se deseja os dados da temporada regular ou dos playoffs. Ele utiliza as bibliotecas requests e pandas para realizar a extração.

### Parâmetros
- `jogador` (str): O nome do jogador que deseja obter os dados.
- `regular_ou_playoffs` (str, opcional): Escolha entre "Regular Season" ou "Playoffs" para especificar o tipo de dados desejados (padrão: "Regular Season").

### Métodos
- `get_dataframe()`: Retorna os dados em um DataFrame.
- `get_json()`: Retorna os dados em formato JSON.

## Módulo TeamGameLogs

### Descrição
O módulo `TeamGameLogs` é responsável por extrair logs de jogos de um time em um ano específico. Ele utiliza as bibliotecas requests e pandas para realizar a extração.

### Parâmetros
- `time` (str): O nome do time para o qual deseja extrair os logs de jogos.
- `ano` (int): O ano para o qual deseja extrair os dados.

### Métodos
- `get_dataframe()`: Retorna os dados em um DataFrame.
- `get_json()`: Retorna os dados em formato JSON.

Com esses módulos, você pode facilmente realizar web scraping de dados relacionados ao futebol americano no site Pro-Football-Focus. Certifique-se de instalar as bibliotecas necessárias antes de usar esses módulos em seu projeto.
