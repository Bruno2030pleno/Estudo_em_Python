def criando():
    lista_de_nomes = {'nome1': 'bruno',
             'nome2': 'lena',
             'nome3': 'miguel'}
    nome_do_arquivo = 'primeiro_arquivo.txt'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        for nome in lista_de_nomes.values():
            arquivo.write(nome + '\n')
    print('arquivo gravado')        
criando()                



