import operator as t
from functools import partial as p
resultado_da_soma = []

def  calculadora(operacao, simbolo, operando_1, operando_2):
    global resultado_da_soma

    if simbolo == '/' and float(operando_2) == 0:
       print('impossivel dividir por zero') 
    
    else:
        resultado = operacao(float(operando_1), float(operando_2))
        resultado_da_soma.append(resultado)
        print(f"dados guardados na lista {resultado_da_soma}")
        print(f"{operando_1} {simbolo} {operando_2} =  {resultado} ")
   
operacoes = {
    '+': p(calculadora, t.add, '+'),
    '-': p(calculadora, t.sub, '-'),
    '*': p(calculadora, t.mul, '*'),
    '/': p(calculadora, t.truediv, '/')
}

     
try:
    while True:
        operando_1 = input('digite o primeiro operando_1: ')
        operando_2 = input('digite o segundo operando_2: ')
        operacao =  input('digite o operador desejado! ').lower().strip()
        
        
        if  operacao in operacoes:
            operacoes[operacao] (operando_1, operando_2)
         
            
        else:
           print('operação invalida! ') 
               
except ValueError:
    print('digite apenas numeros: ') 
except ValueError:
    print('erro, nao e possivel dividir por zero ')
    