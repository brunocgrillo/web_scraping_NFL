from gamelogs.gamelogs import TeamGameLogs
import sys

if sys.version_info.major != 3:
    print('Versão do python não compatível com o pacote')

libs_players = ['pandas', 'requests']

for lib in libs_players:
    try:
        __import__(lib)
    except:
        print(f'Biblioteca {lib}, necessária para o módulo TeamGameLogs, não instalada')