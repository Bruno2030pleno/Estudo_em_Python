# crie um programa que receba uma lista de nomes de arquivos
# e os imprima um por um

# def lista_de_nomes():
#     lista = ['bruno.txt', 'miguel.txt', 'lena.txt']
#     for nome in lista:
#         with open(nome, 'w', encoding='utf-8') as arquivo_atual:
#             arquivo_atual.write('data de nascimento 1991') 
# lista_de_nomes()                
       

# d = input("digite o nome do arquivo").lower()
# with open(d, 'w', encoding='utf-8') as pense:
#     conteudo = input('digite o conteudo do arquivo').lower()
#     pense.write(conteudo)

import os

d = input("Qual arquivo você deseja ler? ").lower()
if os.path.exists(d):
    with open(d, 'r', encoding='utf-8') as lendo:
        t = lendo.read()
        print("\n--- Conteúdo do Arquivo ---")
        print(t)
        print("---------------------------")
else:
    print(f"Erro: O arquivo '{d}' não foi encontrado no diretório atual.")
        
           