def dados():
    d = {}
    
    while True:
        try:
            chave = input('digite a chave: ou sair: ')
            valor = input('digite o valor: ')
            if chave == 'sair':
                break
            else:
                d[chave] = valor
                print(f'valor adicionador {d}')
        except ValueError:
            print('digite apenas letras ')        
dados()            
            