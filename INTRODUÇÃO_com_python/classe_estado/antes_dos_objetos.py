# primeira versão : falha

# ligado = False
# canal = 2
# def ligar_tv():
#     global ligado
#     ligado = True
# def desligar_tv():
#     global ligado
#     ligado = False    

# segunda versão 
tv_sala = {'ligado': False, 'canal': 2}
tv_quarto = {'ligado': False, 'canal': 2}
def ligar_tv(tv):
    tv[ligar_tv] =  True
    

def desligar_tv(tv):
    tv[ligar_tv] = False    
    
ligar_tv(tv_sala)
desligar_tv(tv_quarto)    
 