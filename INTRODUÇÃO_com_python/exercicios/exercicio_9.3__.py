def criando_arquivo():
    with open('pares.txt', 'w') as pares, open('impares.txt', 'w') as impares:
        for linha in range(1,200):
            if linha % 2 == 0:
                convertendo = str(linha)
                pares.write(convertendo + '\n')
            else:
                impares.write(str(linha) + '\n')  
    
    with open('pares.txt', 'r') as pares,  open('impares.txt', 'r') as impares, open('novo.txt', 'w') as novo:
        conteudo = pares.read() + impares.read()
        novo.write(conteudo)
criando_arquivo()                  