def loginUsuario(perfil):
    if perfil.lower() == 'admin':
       return f'ben vindo administrador'
    else:
        return f'Erro, tente novamente'
print(loginUsuario('ADMIN'))
print(loginUsuario('User'))
print(loginUsuario('CONVIDADO'))   
                
