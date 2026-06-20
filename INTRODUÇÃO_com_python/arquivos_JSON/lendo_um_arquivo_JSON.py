# programa 9.15
# lendo um arquivo JSON

import json
from pathlib import Path

# Correto: Uma lista contendo três dicionários distintos
dados = [
    {'nome': 'marcos', 'nota': [5.6, 8.7, 9.8]},
    {'nome': 'bruno', 'nota': [6.9, 7.9, 9.9]},
    {'nome': 'lena', 'nota': [4.6, 6.7, 8.9]}
]
caminho = Path('lista.json')
# Agora, o JSON conterá os 3 registros corretamente
caminho.write_text(json.dumps(dados, indent=4, ensure_ascii=False), encoding='utf-8')


# Se o arquivo já foi gerado antes, essa parte lê corretamente:
with Path('lista.json').open() as arquivo:
    dados = json.load(arquivo)
    for aluno in dados:
        print('nome', aluno['nome'])
        print('nota', aluno['nota'])
        print('media', sum(aluno['nota']) / len(aluno['nota']))
   

