class NovaException(Exception):
    pass

def lançador():
    raise NovaException("Exceção lançada!")  # aqui você lança
   

try:
    lançador()
except NovaException as e:
    print(e)       
