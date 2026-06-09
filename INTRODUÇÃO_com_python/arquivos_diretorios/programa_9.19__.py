# propriedades de um arquivo
import os
import time
import sys
# Pega o nome do arquivo passado como argumento no terminal
nome = sys.argv[1]
print(f'nome: {nome}')
print(f'tamanho: {os.path.getsize(nome)} bytes') # retorna o tamnha do arquivo em bytes
print(f'criado: {time.ctime(os.path.getctime(nome))}') # data e a hora
print(f'modificado: {time.ctime(os.path.getmtime(nome))}') # modificação
print(f'acessado: {time.ctime(os.path.getatime(nome))}') #  acesso




