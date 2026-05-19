# modifique o programa 9.5 para imprimir 40 vezes o simbolo
# de = se este for o primeiro caractere da linha. adicione tambem a opção 
# para parar de imprimir ate que se pressione a tecla enter cada vez que uma linha iniciar 
# com . (ponto) como primeiro caractere


def arquivox():
    print("--- Iniciando o Processamento ---")
    LAGURA = 79
    try:
        
        with open('entrada.txt', 'r', encoding='utf-8') as entrada:
            contador = 0
            for linha in entrada: 
                contador += 1
                linha = linha.strip()
                
                if not linha:
                    continue

                if linha[0] == ';':
                   continue
                
                elif linha[0] == '>':
                    print(linha[1:].rjust(LAGURA)) 
                
                elif linha[0] == '*':
                    print(linha[1:].center(LAGURA)) 
                elif linha[0] == '=':
                    print('=' * 40)
                elif linha[0] == '.':
                    print(linha[1:])
                    ponto = input("digite algo") 
                           
                else:
                    print(linha)  
    except FileNotFoundError:
        print("Erro: O arquivo 'entrada.txt' não foi encontrado.")          
arquivox()