def login_do_usuario():
    email = 'jose'
    senha = '123'
    tentativa = 3
    try:
        for tentativas in range(1, tentativa + 1):
            print(f'tentativas  {tentativas} maximo de tentativas {tentativa}')
            email_1 = input("digite seu email: ")
            if email_1 == email:
                print('email ok') 
                senha_1 = input("digite sua senha: ") 
                if senha_1 == senha:
                    print('login realizado com sucesso')
                    return
            else:
                print('email invalido!!')
            restante = tentativa - tentativas
            if restante > 0:
                print(f' restam {restante}!')
        print(f'login bloqueado')
    except ValueError:
        print('digite apenas letras')
login_do_usuario()    