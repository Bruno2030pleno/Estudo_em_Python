from pathlib import Path as path
def extrair_arquivo():
    nova_lista_de_nomes = []
    arquivo = path("primeiro_arquivo.txt")
    
    if arquivo.exists():
        print('o arquivo existe')
    
        with open(arquivo, 'r', encoding='utf-8') as axtracao_de_arquivo:
            
            for linha in axtracao_de_arquivo:
                
                limpando = linha.strip()
                
                nova_lista_de_nomes.append(limpando)
            
            print(nova_lista_de_nomes) 
        
        for nome in nova_lista_de_nomes:
            print(nome)       
    else:
         print('o arquvo nao existe')
extrair_arquivo()       
