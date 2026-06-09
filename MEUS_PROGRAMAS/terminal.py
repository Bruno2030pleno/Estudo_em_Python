import sys
from pathlib import Path as path

# 1. Verifica se o usuário digitou algo no terminal (tamanho da lista deve ser pelo menos 2)
if len(sys.argv) < 2:
    print('Erro: você precisa passar o nome do arquivo na linha de comando')
    sys.exit(1)

# 2. Pega o nome do arquivo do terminal
arquivo_lendo = sys.argv[1]

# 3. Verifica se existe
if not path(arquivo_lendo).exists():
    print(f"Erro: O arquivo '{arquivo_lendo}' não foi encontrado.")
    sys.exit(1)

# 4. Lê e imprime
with open(arquivo_lendo, 'r', encoding='utf-8') as l:
    leitura = l.read()
    print(leitura)