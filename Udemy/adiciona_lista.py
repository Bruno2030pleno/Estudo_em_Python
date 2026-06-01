def adiciona_lista(nome, lista=[]):
    if lista is not None:
       lista = []     
    lista.append(nome)
    return lista
cliente_1 = adiciona_lista('jose')
adiciona_lista('bruno', cliente_1)
print(cliente_1)


