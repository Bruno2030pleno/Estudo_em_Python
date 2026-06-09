# programa 9.13 
# arvore de diretorios sendo percorrida - com pathlib
import sys 
from pathlib import Path as path

# Corrigido: verifica se o usuário passou o argumento (nome do programa + caminho = 2 elementos)
if len(sys.argv) < 2:
    print('Erro: caminho do diretório faltando')   
    sys.exit(1)

# Loop principal
for raiz, diretorios, arquivos in path(sys.argv[1]).walk():
    print('\ncaminho:', raiz)
    
    for D in diretorios:
        print(f' Diretório: {D}')
        
    for F in arquivos:
        print(f' Arquivo: {F}')
    
    # Corrigido: a contagem deve ficar aqui, após listar tudo daquela pasta
    print(f'Total: {len(diretorios)} diretório(s) e {len(arquivos)} arquivo(s)')