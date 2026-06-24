from collections import UserList
class ListaUnica(UserList):
    
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe
    
    def append(self, item):
        self.verifica_tipo(item)
        if item not in self.data:
            super().append(item)  
        
    def __setitem__(self, posicao, item):
        self.verifica_tipo(item)
        if item not in self.data:
            super().__setitem__(posicao, item)
    
    def verifica_tipo(self, item):
        if not isinstance(item, self.elem_classe):
            raise TabError('tipo invalido!!')
                        
    def extend(self, lista):
        for item in lista:
            self.append(item)
        
      
        