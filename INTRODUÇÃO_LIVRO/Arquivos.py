def arquivo():
    print('bem vindo')
    LISTA_DE_COMPRAS = {
    'MANGA':  {'QUANTIDADE': 1, 'preço': 5.5},
    'ABACATE':{'QUANTIDADE': 1,'preço': 8.6}
}
    with open('aquivos.txt', 'w', encoding='utf-8') as ARQUIVOS:
        for produto, detalhe in LISTA_DE_COMPRAS.items():
            quantidade = detalhe['QUANTIDADE']
            preco = detalhe['preço']
            dados = f'produto {produto} quantidade EM KG {quantidade} preço R$ {preco}\n'
            ARQUIVOS.write(dados)
    
arquivo() 

# DE INICIO EU CRIE UMA FUNÇÃO PARA PODER CRIAR UM ARQUIVO 
# MAS EU TIVE UMA IDEIA DE EXTRAIR OS DADOS DO DICIONARIO E CRIAR UMA ARQUIVO COM ESSES DADOS  


