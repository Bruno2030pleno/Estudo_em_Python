
# class Nome:
#     def __init__(self, name):
#         if name is None or not name.strip():
#            raise ValueError('nome não pode ser nulo nem em branco')
#         self. nome = name
#         self.chave = name.strip().lower()
#     def __str__(self):
#         return self.nome  # atributo definido no __init__
    
#     def __repr__(self):
#         return f"Class {type(self).__name__} em 0x{id(self):x} nome: {self.nome} chave: {self.chave}>"

#     def __eq__(self, outro):
#         return self.nome == outro.nome
    
#     def __lt__(self, outro):
#         return self.chave < outro.chave 
    
#     @staticmethod
#     def CriaChave(name):
#         return name.strip().lower()    




# @total_ordering
# class Nome:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, valor):
#         if valor is None or not valor.strip():
#             raise ValueError("name não pode ser nulo nem em branco")
#         self.__name = valor
#         self.__chave = Nome.CriaChave(valor)

#     @property
#     def chave(self):
#         return self.__chave

#     def __str__(self):
#         return self.__name

#     def __repr__(self):
#         return f"<Class {type(self).__name__} em 0x{id(self):x} nome: {self.__name} chave: {self.__chave}>"

#     def __eq__(self, outro):
#         return self.__chave == outro.__chave

#     def __lt__(self, outro):
#         return self.__chave < outro.__chave

#     @staticmethod
#     def CriaChave(name):
#         return name.strip().lower()
from functools import total_ordering
@total_ordering   
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"<Class {type(self).__name__} em 0x{id(self):x} nome: {self.__name} chave: {self.__chave}>"
    def __eq__(self, outro):
       return self.__chave == outro.__chave 
    def __lt__(self, outro):
        return self.__chave < outro.__chave 
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, valor):
        if valor is None or not valor.strip():
            raise  ValueError("name não pode ser nulo nem em branco")
        self.__name = valor
        self.__chave = Name.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def CriaChave(name):
        return name.strip().lower() 

            