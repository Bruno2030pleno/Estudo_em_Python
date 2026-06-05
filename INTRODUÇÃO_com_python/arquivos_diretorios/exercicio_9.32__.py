# modifique o programa 9.9  de forma a receber o nome do arquivo
# ou diretorio a verifiar pela linha de comando. imprima se existir se for um arquivo ou um diretorio

import os.path 
import sys

if len(sys.argv) < 2:
    print("Erro: Você precisa informar o nome do arquivo ou diretório.")
    print("Uso: python exercicio_9.32__.py <nome_para_verificar>")
else:
    b = sys.argv[1]
    
    if os.path.exists(b):
        if os.path.isdir(b):
            print(f"'{b}' existe e é um diretório.")
        elif os.path.isfile(b):
            print(f"O caminho '{b}' existe e é um arquivo.")
    else:
        print(f"O caminho '{b}' não existe.")