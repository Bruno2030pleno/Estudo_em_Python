def ocorrencia_no_arquivo():

    dicionario = {}
    
    with open('bruno.txt', 'r') as leitura:
        
        for nun_linha, texto_linha in enumerate(leitura, 1):
            
            tratamento = texto_linha.lower().split()
            
            for palavra in  tratamento:
                
                coluna =  texto_linha.lower().find(palavra)
                
                if palavra in dicionario:
                    dicionario[palavra].append([nun_linha, coluna]) 
                else:
                    
                    dicionario[palavra] = [[nun_linha, coluna]]

        print(dicionario)                

ocorrencia_no_arquivo()

