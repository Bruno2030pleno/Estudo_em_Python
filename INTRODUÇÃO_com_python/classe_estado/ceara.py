class Estado:
    def __init__(self,estado, cidade, populacao):
        self.estado =estado
        self.cidade = cidade
        self.populacao = populacao
    
    def exibir_nomes_das_cidade(self, sicla):
        print(f'\nMeu estado {sicla} ({self.estado}) Nome da cidade ({self.cidade})')
        

    def quantidade_da_populacao(self):
        print(f'Quantidade da população ({self.populacao})') 

cidade_ceara = Estado('CEARA', 'FORTALEZA', 'Cerca de 2,6 milhões de pessoas'  )
cidade_mata_grosso = Estado('MATO GROSSO', 'CUIABÁ', ' Cerca de  650.877 residentes.') 
cidade_santa_catarina = Estado('santa catarina', 'Florianópolis', 'Cerca de 587.486 habitantes,') 

cidade_mata_grosso.exibir_nomes_das_cidade('MT')
cidade_mata_grosso.quantidade_da_populacao()

cidade_ceara.exibir_nomes_das_cidade('CE')
cidade_ceara.quantidade_da_populacao()

cidade_santa_catarina.exibir_nomes_das_cidade('SC')
cidade_santa_catarina.quantidade_da_populacao()

class governo:
    def __init__(self):
        pass