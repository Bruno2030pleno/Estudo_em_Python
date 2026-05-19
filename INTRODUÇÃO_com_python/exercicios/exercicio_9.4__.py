import sys 
def parametros():

    try:
        if len(sys.argv) == 4:

            entrada_1 = sys.argv[1]
            entrada_2 = sys.argv[2]
            arquivo = sys.argv[3]
            
            with open(entrada_1, 'r') as E1: 
                conteudo_1 = E1.read()  
            
            with open(entrada_2, 'r') as E2:
                conteudo_2 = E2.read()

            with open(arquivo, 'w') as recebendo_arquivos:

                recebendo_arquivos.write(conteudo_1 + conteudo_2)    

    except Exception as Erro:
        print(f"Ocorreu um erro inesperado: {Erro}")     
parametros()               
               



    