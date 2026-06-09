# import pathlib as path
# caminho = path('INTRODUÇÃO_com_python') / 'verificar.txt'
# if caminho.exist():
#     print('o caminho e o arquivo existe')
# else:
#     print('erro')    


from pathlib import Path
import os

# print(f"Diretório onde o Python está rodando: {os.getcwd()}")

# # Tente listar o que ele enxerga dentro da pasta que você definiu:
# pasta_alvo = Path('Estudo_em_Python/INTRODUÇÃO_com_python/pathlib')
# if pasta_alvo.exists():
#     print("A pasta existe! Conteúdo dela:")
#     for item in pasta_alvo.iterdir():
#         print(f" - {item.name}")
# else:
#     print("A pasta não foi encontrada. Verifique se você está na pasta pai correta.")         

from pathlib import Path

# Se você estiver na pasta 'Estudo_em_Python', este caminho está perfeito:
pasta_alvo = Path('INTRODUÇÃO_com_python/Pathlib') / 'verificar.txt'

if pasta_alvo.exists():
    print(f"Sucesso! Encontrei a pasta: {pasta_alvo.resolve()}")
else:
    print(f"Caminho não encontrado. Eu procurei em: {pasta_alvo.absolute()}")