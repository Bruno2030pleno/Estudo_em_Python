def ocorrencia_no_arquivo():
    dicionario = {}
    with open('bruno.txt', 'r') as leitura:
        for chave in leitura:
            tratamento = chave.lower().split()
            for palavra in  tratamento:
                if palavra in dicionario:
                    dicionario[palavra] += 1
                else:
                    dicionario[palavra] = 1
        print(dicionario)                
ocorrencia_no_arquivo()

         
