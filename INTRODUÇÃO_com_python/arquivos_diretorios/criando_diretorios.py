import os.path

# os.mkdir('d')
# os.mkdir('e')
# os.mkdir('f')
# print(os.getcwd())
# os.mkdir('d')
# print(os.getcwd())
# os.chdir('../e')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# os.chdir('f')
# print(os.getcwd())


# 1. Cria a estrutura com o filho do pai
# os.makedirs('avo/pai/filho/bebe')

# 2. Cria a estrutura APENAS até a mãe (sem o filho)
# os.makedirs('avo/mae')

# 3. Move (renomeia) o filho do pai para a mãe
# os.rename('avo/pai/filho/bebe', 'avo/mae/bebe')
# os.mkdir('velho')
# os.rename('velho', 'novo')

# os.rmdir('f')

# criar um  arquivo e o fechar imediatamente
# open('morimbundo.txt', 'w').close()
# os.mkdir('vago')
# os.rmdir('vago')
# os.remove('morimbundo.txt')

# print(os.listdir('.'))
# print(os.listdir('avo'))
# print(os.listdir('avo/pai'))
# print(os.listdir('avo/mae'))

# for lista in os.listdir('avo'):
#     print(lista)

# for lista in os.listdir('.'):
    
#     if os.path.isdir(lista):
#         print(f'{lista}/')
    
#     elif os.path.isfile(lista):
#         print(lista)    

# 9.11 UM POUCO SOBRE O TEMPO
# import time
# # agora = time.time()
# # agora = time.ctime()
# agora = time.localtime()
# # agora = time.gmtime()
# lista = []
# for tapla in agora:
#    lista.append(tapla)
# ano = lista[0]
# mes = lista[2]
# dia = lista[4]
# print(f'ano {ano}')
# print(f'mes {mes}')
# print(f'dia {dia}')
# print(lista)


# import time

# agora = time.localtime()

# ano = agora.tm_year
# mes = agora.tm_mon
# dia = agora.tm_mday
# hora = agora.tm_hour 

# print(f'ano {ano}')
# print(f'mes {mes}')
# print(f'dia {dia}')
# print(f'{hora} horas')


# programa 9.11 exibindo os componetes da data e hora

# import time

# agora = time.localtime()

# ano = agora.tm_year
# mes = agora.tm_mon
# dia = agora.tm_mday
# hora = agora.tm_hour 

# print(f'ano {ano}')
# print(f'mes {mes}')
# print(f'dia {dia}')
# print(f'{hora} horas')

# print(time.strftime('%a/%d/%b/%j'))

# caminho = 'MEUS_PROGRAMAS//novo'
# d = os.path.splitdrive('nova_lista.br')
# print(d)
# d = os.path.splitext('nova_lista.br')
# print(d)

teste = os.path.join('c:', 'dados', 'programas')
print(teste)

teste1 = os.path.abspath(os.path.join('c:', 'dados', 'programas'))
print(teste1)