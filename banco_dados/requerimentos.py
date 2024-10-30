#!python3
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connerctor não instalado!')
else:
    print('MySQL Connector instalado e pronto!')