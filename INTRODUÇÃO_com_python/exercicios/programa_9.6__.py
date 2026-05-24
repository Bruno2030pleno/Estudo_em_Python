# controle de uma agenda de telefone
agenda = []
foi_alterada = False
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
def ordena():
    global foi_alterada
    foi_alterada = True
    agenda.sort()
    print('\nAgenda ordenada com sucesso por ordem alfabética!')
    
def novo():
    global foi_alterada
    foi_alterada = True
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    

def apaga():
    apagar = input('deseja exluir o nome sim ou nao ?').strip().lower()
    global foi_alterada 
    
    if apagar == 'sim' :  
        nome = pede_nome()
        p = pesquisa(nome)
        if p is not None:
            del agenda[p]
            foi_alterada = True
            
            print('nome apagado com sucesso')    
        else:
            print('nome nao encontrado')
    else:
        print('O nome não foi apagado!!: ')           
def altera():
    alterar = input('deseja altera o nome ?: sim ou nao: ').strip().lower()
    global foi_alterada
    if alterar == 'sim':
        p = pesquisa(pede_nome())       
        if p is not None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            print('encontrado!!')
            mostra_dados(nome, telefone)
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
            foi_alterada = True
        else:
            print('nome nao encontrado')
    else:
        print('O nome não foi alterado: ')
def lista():
    global foi_alterada
    global agenda
    print('\nAgenda\n\n------')       
    for e, i in enumerate(agenda):
        mostra_dados(i[0], i[1])
        print(f'posição {e}')
    print(f'tamanho da agenda {len(agenda)}') # modifiquei 
    print('------\n')

def ler():
    global foi_alterada
    global agenda
    if foi_alterada:
       confirma = input('Você tem alterações não salvas. Deseja ler um novo arquivo e perder os dados atuais? (s/n): ').strip().lower()
       if confirma != 's':
           return 
    try:
        nome_arquivo = pede_nome_arquivo()  
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: 
            agenda = []
            for linha in arquivo.readlines():
                nome, telefone = linha.strip().split('#')
                agenda.append([nome, telefone])
        foi_alterada = False
    except FileNotFoundError:
        print('ERRO DESCONNHECIDO:: ')         

def grava():
    arquivo_extra = 'lembrete.txt'
    global foi_alterada
    foi_alterada = False
    try:
        nome_arquivo = pede_nome_arquivo()  
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for e in agenda:
                arquivo.write(f'{e[0]}#{e[1]}\n') 
        
        with open(arquivo_extra, 'w', encoding='uft-8') as lembrete:
            for n in agenda:
               lembrete.write(n)
    
    except FileNotFoundError:
        print('NAO FOI POSSIVEL GRAVAR O ARQUIVO: ')        

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
7 - ordenar - nome
0 - sai 
""")
    return validar_faixa_inteiro('escolha uma opção (0 a 7): ', 0, 7) 

while True:
    opcao = menu()
    if opcao == 0:
        if foi_alterada:
            salvar = input("Você tem alterações não salvas. Deseja gravar antes de sair? (s/n): ").strip().lower()
            if  salvar == 's':
                grava()
        print('fim do programa:  todos os dados foram salvos com sucesso! ')    
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
        ler()
    elif opcao == 7:
        ordena()

    

