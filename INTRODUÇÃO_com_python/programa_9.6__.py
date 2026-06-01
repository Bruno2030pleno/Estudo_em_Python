# controle de uma agenda de telefone
agenda = []
foi_alterada = False
def pede_nome(padrao='jose'):
    entrada = input('nome: ')
    if entrada == '':
        return padrao        
    else:
        return entrada

def pede_telefone(telefones_antigos=None):
    if telefones_antigos is None:
        telefones_antigos = []
    lista_telefones = []
    if telefones_antigos:
        print(" [Pressione Enter sem digitar para manter os telefones atuais]")
    while True:
        numero = input("telefone (ou Enter para sair): ")
        if numero == '':
            break
        tipo = input("Qual o tipo desse telefone? (celular, fixo, trabalho): ")
        lista_telefones.append([tipo, numero])
        
    if not lista_telefones and telefones_antigos:
        return telefones_antigos
    return lista_telefones

def pede_aniversario(padrao=''):
    aniversario = input('qual a data de anivesario ?: ')
    if aniversario == '':
        return padrao
    else:
        return aniversario
        
def pede_email(padrao=''):
    email = input('qual o email ? ')
    if email == '':
        return padrao
    else:
        return email
            
def mostra_dados(nome, telefones, email, aniversario):
    print(f'Nome: {nome} | Email: {email} | Aniversário: {aniversario}')
    print('Telefones:')
    if isinstance(telefones, list):
        for t in telefones:
            print(f'  - {t[0]}: {t[1]}')
    else:
        print(f'  - {telefones}')
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
    nome = pede_nome()
    posicao = pesquisa(nome)
    if posicao is not None:
       print("Erro: Esse nome já existe na agenda!") 
       return
    telefone = pede_telefone()
    email = pede_email()
    aniversario = pede_aniversario()
    agenda.append([nome, telefone, email, aniversario])
    foi_alterada = True
    
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
            email = agenda[p][2]
            aniver = agenda[p][3]
            print('encontrado!!')
            mostra_dados(nome, telefone, email, aniver)
            nome = pede_nome(nome)
            telefone = pede_telefone(telefone)
            email = pede_email(email)
            aniver = pede_aniversario(aniver)
            agenda[p] = [nome, telefone, email, aniver]
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
        mostra_dados(i[0], i[1], i[2], i[3])
        print(f'posição {e}')
    print(f'tamanho da agenda {len(agenda)}') # modifiquei 
    print('------\n')

def ler():
    global foi_alterada
    global agenda
    arquivo_extra = 'lembrete.txt'
    if foi_alterada:
       confirma = input('Você tem alterações não salvas. Deseja ler um novo arquivo e perder os dados atuais? (s/n): ').strip().lower()
       if confirma != 's':
           return 
    try:
        nome_arquivo = pede_nome_arquivo()  
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: 
            agenda = []
            print("\n--- Carregando Contatos ---")
            for linha in arquivo:
                print(linha, end='')
                if '#' in linha:
                    partes = linha.strip().split('#')
                    nome = partes[0]
                    tel_str = partes[1] if len(partes) > 1 else ""
                    email = partes[2] if len(partes) > 2 else ""
                    aniversario = partes[3] if len(partes) > 3 else ""
                    telefones = []
                    if tel_str:
                        for par in tel_str.split(';'):
                            if ':' in par:
                                tipo, num = par.split(':', 1)
                                telefones.append([tipo, num])
                            else:
                                telefones.append(['geral', par])
                    agenda.append([nome, telefones, email, aniversario]) 
            print("\n---------------------------")
        with open(arquivo_extra, 'w', encoding='utf-8') as lembrete:
               lembrete.write(nome_arquivo)
        foi_alterada = False
    except FileNotFoundError:
        print('o arquivo não foi encontrado na pasta atual: ')         

def grava():
    arquivo_extra = 'lembrete.txt'
    global foi_alterada
    foi_alterada = False
    try:
        nome_arquivo = pede_nome_arquivo()  
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for e in agenda:
                telefones = e[1]
                if isinstance(telefones, list):
                    tel_str = ';'.join([f'{t[0]}:{t[1]}' for t in telefones])
                else:
                    tel_str = telefones
                arquivo.write(f'{e[0]}#{tel_str}#{e[2]}#{e[3]}\n') 
        with open(arquivo_extra, 'w', encoding='utf-8') as lembrete:
               
               lembrete.write(nome_arquivo)

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
6 - ler
7 - ordenar - nome
0 - sai 
""")
    return validar_faixa_inteiro('escolha uma opção (0 a 7): ', 0, 7) 
try:
    arquivo_extra = 'lembrete.txt'
    with open(arquivo_extra, 'r', encoding='utf-8') as leitura:
        ultima_agenda = leitura.read().strip()
        print(f'aquivo {ultima_agenda}')
    with open(ultima_agenda, 'r', encoding='utf-8') as novos:
        for n in novos:
            if '#' in n:
                partes = n.strip().split('#')
                nome = partes[0]
                tel_str = partes[1] if len(partes) > 1 else ""
                email = partes[2] if len(partes) > 2 else ""
                aniversario = partes[3] if len(partes) > 3 else ""
                telefones = []
                if tel_str:
                    for par in tel_str.split(';'):
                        if ':' in par:
                            tipo, num = par.split(':', 1)
                            telefones.append([tipo, num])
                        else:
                            telefones.append(['geral', par])
                agenda.append([nome, telefones, email, aniversario])
except FileNotFoundError:
    pass
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
   
    
