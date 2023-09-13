from leagueleaders import LeagueLeaders2
import sys

if sys.version_info.major != 3:
    print('Versão do python não compatível com o pacote')

libs_leagueleaders = ['selenium', 'webdriver_manager', 'bs4']

for lib in libs_leagueleaders:
    try:
        __import__(lib)
    except:
        print(f'Biblioteca {lib}, necessária para o primeiro módulo, não instalada')

libs_leagueleaders2 = ['requests', 'pandas']

for lib in libs_leagueleaders2:
    try:
        __import__(lib)
    except:
        print(f'Biblioteca {lib}, necessária para o primeiro módulo, não instalada')