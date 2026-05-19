# def criar_varios_arquivos(quantidade):
#     for i in range(quantidade):
#         nome_arquivo = f'arquivo_{i}.txt'
#         with open(nome_arquivo, 'w') as f:
#             f.write(f'Este é o arquivo número {i}')
#         print(f'{nome_arquivo} criado com sucesso!')

# # Cria 3 arquivos de uma vez
# criar_varios_arquivos(3)

def criar_arquivo():
    lista = []
    while True:
        entrada = input('digite algo, ou sair')
        if entrada == 'fim':
            print('--- FIM DO SISTEMA ---')
            break
        
        lista.append(entrada)
        print(f'dados adiocionados {lista}')
        
        with open('nova_lista.txt', 'w') as dados_na_lista:
            for lista_1 in lista:
                dados_na_lista.write(f'{lista_1}')
        print("Arquivo 'nova_lista.txt' criado com sucesso!")            
criar_arquivo()                           