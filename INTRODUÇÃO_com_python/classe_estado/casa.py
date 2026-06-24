class casa:
    def __init__(self, abrindo_porta, entrando_na_casa):
        self.abrindo_porta = abrindo_porta
        self.entrando_na_casa = entrando_na_casa
        self.chave = False
    
    def acessando(self,tem_chave):
        if tem_chave:
           self.chave == True
           return True
        return False   
      
       
                  
entrando = casa('abrindo a porta', 'entrando na casa')

pessoa = input('você tem a chave ? s/n: ').lower().strip()

tem_chave = (pessoa == 's')

if entrando.acessando(tem_chave):
    print(f'Sucesso: {entrando.abrindo_porta} : {entrando.entrando_na_casa}.')
else:
    print('Acesso negado: você não tem a chave.')
