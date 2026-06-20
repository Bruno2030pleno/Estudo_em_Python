import json
from pathlib import Path as path
def adicionando_dados():
    caminho = path('salvando_em_json.json')
    agenda = {}
    while True:
        nome = input('digite os dados da agenda: ou enter em branco para sair  ')
        if not nome:
            break
        tel = int(input("digite o telefone: "))
        if not nome:
            break
        agenda[nome] = tel
        caminho.write_text(json.dumps(agenda, indent=4, ensure_ascii=False), encoding='utf-8')
        print("\nDados gravados com sucesso!\n")
adicionando_dados()        