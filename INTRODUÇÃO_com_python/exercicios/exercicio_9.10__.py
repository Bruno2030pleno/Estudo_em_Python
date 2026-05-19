def lista_de_arquivos():
    lista_de_nomes = ['bruno.txt','entrada.txt','doc.txt']
    with open('arquivo_geral.txt', 'a', encoding='utf-8') as arquivo_de_destino:
        for nomes in lista_de_nomes:
            
            try:
                with  open(nomes, 'r', encoding='utf-8') as origem:
                    conteudo = origem.read()
                    arquivo_de_destino.write(conteudo + '\n')
            
            except FileNotFoundError:
                print('nome nao encontrado no arquivo')
lista_de_arquivos()         