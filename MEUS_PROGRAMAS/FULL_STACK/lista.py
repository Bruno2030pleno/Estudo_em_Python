def adicionar_dados():
    lista = []
    while True:
        
        dados = input('digite qualquer coisa: ').lower().strip()
        lista.append(dados)
        print(f'dados na lista {lista}')
        
        sim_ou_nao = input('consultar indice sim ou nao ?: ou sair:  ')
        
        if sim_ou_nao == 'sim':
            try:
                consultar = int(input('digite o indice: '))
                indice = lista[consultar]
                print(indice)   
            except ValueError:
                print('por favor digite apenas numetos')
            except IndexError:
                print(f'por favor digite o indice correto!: {len(lista)} ') 
        else:
            sim_ou_nao == 'sair'
            break                   
adicionar_dados()          
                


