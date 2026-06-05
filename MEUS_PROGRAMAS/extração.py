def extrair_arquivos():
    dados_extraidos = []
    arquivos_beta = 'arquivo_beta.txt'
    try:
        with open(arquivos_beta, 'r', encoding='utf-8') as extracao:
            leitura = extracao.readlines()
            for dados in leitura:
                limpeza = dados.strip()
                dados_extraidos.append(limpeza)
                print(f'{limpeza}')
    except FileNotFoundError:   
        print('Erro: o arquivo nao foi encontrado no diretorio')
        return
    
    escolha = input('escolha qual linguagem para gravar no arquivo,(python)-(java)-(c)-(javascript)')
    nova_lista = []
    if escolha in dados_extraidos:
        nova_lista.append(escolha)
        extração_maxima = 'extração_de_dados.txt'
        with open(extração_maxima, 'w', encoding='utf-8') as python:
                python.write(escolha) 
                print('arquivo gravado com sucesso')    
    else:
        print('Erro: elemento não existe na lista de arquivos')
extrair_arquivos()            