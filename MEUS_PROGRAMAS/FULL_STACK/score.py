
def pontuacao_de_score(digitado ,baixo, medio, alto):
    if digitado < baixo:
        return 'seu score esta baixo'
    elif digitado < medio:
        return 'seu score  está na media'
    elif digitado < alto:
        return 'seu score está alto'
    else:
        print('erro no seu score')
b = int(input('Defina o limite para "Baixo": '))
m = int(input('Defina o limite para "Médio": '))
a = int(input('Defina o limite para "Alto": '))

meu_score = int(input('Qual o seu score atual? '))
r = pontuacao_de_score(meu_score, b, m, a)
print(r)
 

    
  