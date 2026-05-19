# def definir_arquivo():
#     nome_do_arquivo = 'escrita_e_leitura'
#     # with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo: # aqui eu vou criar um arquivo ou apagar e fazer outro
#     #     arquivo.write('bruno?')
    
#     with open(nome_do_arquivo, 'a', encoding='utf-8') as sem_apagar: # adicionar na ultima posição
#         sem_apagar.write('<<<_nono.\n')    
    
#     with open(nome_do_arquivo, 'r', encoding='utf-8') as ler: # ler o arquivo 
#         resumo = ler.read()
#         print(resumo) # tenho que sempre colocar read() se eu quiser mostrar na tela   
# definir_arquivo()        

import json
# d = {
#     1: 'bruno',
#      2: 'lena',
#      2: 'miguel',
# 'ende': [{'rua': 'b','n': 10}]
nome_arquivo = 'dicionario_dados.json'

# with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
#     json.dump(d, arquivo, ensure_ascii=False, indent=2)
   
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    d = json.load(arquivo)
    for f in d:
       print(f)
    
   
   
    
        