# propriedades de um arquivo

# import os
# import time
# import sys

# # Pega o nome do arquivo passado como argumento no terminal
# nome = sys.argv[1]

# print(f'nome: {nome}')
# print(f'tamanho: {os.path.getsize(nome)} bytes') # retorna o tamnha do arquivo em bytes
# print(f'criado: {time.ctime(os.path.getctime(nome))}') # data e a hora
# print(f'modificado: {time.ctime(os.path.getmtime(nome))}') # modificação
# print(f'acessado: {time.ctime(os.path.getatime(nome))}') #  acesso




import os
import time
import sys

# Pega o caminho da pasta passado como argumento no terminal
diretorio = sys.argv[1]

print(f"Analisando arquivos no diretório: {diretorio}\n")

# O laço for itera sobre cada item retornado por os.listdir
for nome_arquivo in os.listdir(diretorio):
    
    # Monta o caminho completo para o sistema operacional encontrar o arquivo
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    
    # Verifica se o item é realmente um arquivo (ignorando subpastas)
    if os.path.isfile(caminho_completo):
        print('-' * 40)
        print(f'nome: {nome_arquivo}')
        print(f'tamanho: {os.path.getsize(caminho_completo)} bytes')
        print(f'criado: {time.ctime(os.path.getctime(caminho_completo))}')
        print(f'modificado: {time.ctime(os.path.getmtime(caminho_completo))}')
        print(f'acessado: {time.ctime(os.path.getatime(caminho_completo))}')