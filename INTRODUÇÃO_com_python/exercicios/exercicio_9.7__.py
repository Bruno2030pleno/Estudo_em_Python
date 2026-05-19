# crie um porgrama que leia um arquivo de texto e gere um arquivo de  saida
# paginado. cada linha nao deve conter mais de 76 caracteres. cada pagina tera no maximo 60 linhas
# adicione na ultima linha da pagina o numero da pagina
# atual e o nome do arquivo original

def criar_arquivo_9_7():
    nome_original = 'criacao.txt'
    with open(nome_original, 'r', encoding='utf-8') as entrada, \
         open('saida_paginada.txt', 'w', encoding='utf-8') as saida:
        linhas_na_pagina = 0
        numero_pagina = 1
        for linha in entrada:
            linha = linha.rstrip()[:76]
            if linhas_na_pagina == 60:
                rodape = f"{nome_original} - Página {numero_pagina}"
                saida.write(f"\n{rodape}\n\n") 
                linhas_na_pagina = 0
                numero_pagina += 1
            saida.write(linha + "\n")
            linhas_na_pagina += 1
        if linhas_na_pagina > 0:
            while linhas_na_pagina < 60:
                saida.write("\n")
                linhas_na_pagina += 1
            rodape_final = f"{nome_original} - Página {numero_pagina}"
            saida.write(f"\n{rodape_final}\n")
criar_arquivo_9_7()

