# esse pequeno codigo ele foi desenvolvido com uma porcentagem de 98% por me 
# toda a escrita, tive um pequena ajuda do GEMINI  em relação ao posissionamento da condicional if not adicionar
import json
from pathlib import Path as path
def salvando():
    lista_de_frutas = []
    caminho = path('lista_de_frutas.json')
    while True:
        adicionar = input("digite uma fruta: ou entrer para sair")
        if not adicionar:
            criar = input("você deseja criar um arquivo em json S/N ?: ").lower().strip()
            if criar == 's':
                caminho.write_text(json.dumps(lista_de_frutas, indent=4, ensure_ascii=False), encoding='utf-8')
                print("\nDados gravados com sucesso!\n")
            break
        lista_de_frutas.append(adicionar)
        print('--- LISTA DE FRUSTAS ---')
        print(f"fruta adicionadas com sucesso {adicionar}")
        for fruta in lista_de_frutas:
            print(fruta)
salvando()  
   
   
    
