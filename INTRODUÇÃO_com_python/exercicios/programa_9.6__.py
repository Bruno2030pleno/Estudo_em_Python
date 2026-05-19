# controle de uma agenda de telefone
agenda = []

def pede_nome():
    return input('nome: ')         

def pede_telefone():
    return input('telefone: ')     

def mostra_dados(nome, telefone):
    print(f'nome: {nome} telefone: {telefone}')

def pede_nome_arquivo():
    return input('nome do arquivo: ')

def pesquisa(nome):
    nnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == nnome:
            return p
    return None

def novo():
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    

def apaga():
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print('nome nao encontrado')

def altera():
    p = pesquisa(pede_nome())       
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('encontrado!!')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('nome nao encontrado')

def lista():
    print('\nAgenda\n\n------')       
    for e in agenda:
        mostra_dados(e[0], e[1])
        print(f'tamanho da agenda {len(agenda)}') # modifiquei 
        print('------\n')

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()  
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: 
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split('#')
            agenda.append([nome, telefone])

def grava():
    nome_arquivo = pede_nome_arquivo()  
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')  

def validar_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'valor invalido!, digite entre {inicio} e {fim}')

def menu():
    print(
""" 
1 - novo
2 - altera
3 - apagar
4 - lista
5 - grava
6 - le
7 - pesquisa
0 - sai """)
    return validar_faixa_inteiro('escolha uma opção (0 a 6): ', 0, 6) 

while True:
    opcao = menu()
    if opcao == 0:
        print("Saindo...")
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        pesquisa()

