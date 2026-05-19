# modifique o programa do exercicio 9.7 para tambem receber
# numero de carectere por linha e o numero de linhas por paginas pela linha de comando

import sys

def criar_arquivo_9_7():


    arquivo = sys.argv[1]
    por_linha = int(sys.argv[2])
    por_pagina = int(sys.argv[3])
    
   
    with open(arquivo, 'r', encoding='utf-8') as entrada, \
         open('saida_paginada.txt', 'w', encoding='utf-8') as saida:
        
        linhas_na_pagina = 0
        numero_pagina = 1

        for linha in entrada:
            linha = linha.rstrip()[:por_linha]

            if linhas_na_pagina == por_pagina:
                rodape = f"{arquivo} - Página {numero_pagina}"
                
                saida.write(f"\n{rodape}\n\n") 
                linhas_na_pagina = 0
                numero_pagina += 1

            saida.write(linha + "\n")
            linhas_na_pagina += 1

        if linhas_na_pagina > 0:
            while linhas_na_pagina < por_pagina:
                saida.write("\n")
                linhas_na_pagina += 1
            rodape_final = f"{arquivo} - Página {numero_pagina}"
            saida.write(f"\n{rodape_final}\n")

criar_arquivo_9_7()