def arquivox():
    LAGURA = 79
    try:
        with open('entrada.txt', 'r') as entrada:
            
            for linha in entrada: 
                
                linha = linha.strip()
                
                if not linha:
                    continue
                
                if linha[0] == ';':
                   continue
                
                elif linha[0] == '>':
                    print(linha[1:].rjust(LAGURA)) 
                
                elif linha[0] == '*':
                    print(linha[1:].center(LAGURA)) 
                else:
                    print(linha)  
    except FileNotFoundError:
        print("Erro: O arquivo 'entrada.txt' não foi encontrado.")          
arquivox()
