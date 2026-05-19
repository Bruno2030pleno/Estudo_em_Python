# crie um programa que inverta a ordem das linhas do arquivo pares.txt
# a primeira linha deve conter o maior numero:
# e a ultima o menor

def inverter_a_ordem():
    dados = []
    print('----Arquivo----')
    
    print('---------------')
    with open('pares.txt', 'w') as pares:
        for p in range(1,101, 2):
           pares.write(str(p) + '\n')   
    with open('pares.txt', 'r') as pares: 
        for m in pares:
            dados.append(int(m))
    dados.sort(reverse=True)     
    with open('pares.txt', 'w') as pares: 
        for i in dados:
            pares.write(str(i) + '\n')     
inverter_a_ordem()          



