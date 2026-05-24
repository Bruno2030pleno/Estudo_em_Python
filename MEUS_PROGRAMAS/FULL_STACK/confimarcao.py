def nome():
    nome = 'jose'
    while True:
        entrada = input('digite o seu nome: ')
        if entrada == nome:
            print (f'acesso permitido:')
            break
        else:
            print(f'acesso negado: nome invalido!! {entrada}')    
nome()