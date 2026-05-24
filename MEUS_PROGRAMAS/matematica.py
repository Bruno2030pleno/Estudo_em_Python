n = int(input("digite qualquer numero: "))
operador = input('digite o operador + - * / ')
fixo = int(input('digite o segundo numero:  '))

if operador == '+':
   RESULTADO_1 = n + fixo
   print('----RESUMO DA OPERAÇÃO----')
   print(f'OPERAÇÃO +:  SOMA {RESULTADO_1} ')

elif operador == '-':
    RESULTADO_2 = n - fixo
    print('----RESUMO DA OPERAÇÃO----')
    print(f'OPERAÇÃO -:  SOMA {RESULTADO_2} ')

elif operador == '*':
   RESULTADO_3 = n * fixo
   print('----RESUMO DA OPERAÇÃO----')
   print(f'OPERAÇÃO *:  SOMA {RESULTADO_3} ')

elif operador == '/':  
    if   fixo == 0: 
        print('Erro, impossivel dividir por zero!!')
    else:
        RESULTADO_4 = n / fixo
        print('----RESUMO DA OPERAÇÃO----')
        print(f'OPERAÇÃO /:  SOMA {RESULTADO_4} ')



