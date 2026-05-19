# ESCREVA UM PROGRAMA QUE RECEBA O NOME DE UM ARQUIVO
# PELA LINHA DE COMANDO  E QUE IMPRIMA TODAS AS LINHAS DESSE ARQUIVO

import sys
def criando_arquivo():
    try:
        if len(sys.argv) > 3: 
            arquivo_novo = sys.argv[1]
            inicio = sys.argv[2]
            fim = sys.argv[3]

            with open(arquivo_novo, 'w') as novo: 
                novo.write(f'{inicio} = {fim}') 
                
                print("--- Conteúdo do Arquivo ---")
                print("---------------------------")
                print(f' arquivo {novo} ') 
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
criando_arquivo()        