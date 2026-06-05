# crie um programa que corrija o programa 9.9 de forma a verificar se z existe e é um diretoria
import os.path

if os.path.exists('b'):
    if os.path.isdir('b'):
        print("O diretório b existe")
    else:
        print("b existe, mas é um arquivo, não um diretório")
else:
    print('o diretorio b nao existe') 
