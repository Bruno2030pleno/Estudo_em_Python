# programa 9.17 
# criando uma tabela de preço em json
import json
from pathlib import Path as path

tabela_de_preco = {}

caminho = path('preços.json')
if caminho.exists():
    tabela_de_preco = json.loads(caminho.read_text(encoding='utf-8'))

print('criador da tabela de preços')
print('digite um nome do produto em branco para terminar')

while produto := input('nome do produto'):
    preco = input('preço: ')
    tabela_de_preco[produto] = preco
    caminho.write_text(json.dumps(tabela_de_preco, indent=4, ensure_ascii=False), encoding='utf-8')
    break