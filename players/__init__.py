from players.players import Players
import sys

if sys.version_info.major != 3:
    print('Versão do python não compatível com o pacote')

libs_players = ['bs4', 'pandas', 'requests']

for lib in libs_players:
    try:
        __import__(lib)
    except:
        print(f'Biblioteca {lib}, necessária para o primeiro módulo, não instalada')