# altere o programa 7.2 o jogo forca. dessa vez utilize as funçoes
# de tempo para conometrar a duração das partidas

# programa 7.2  jogo da forca
import time
palavra = input('digite a palavra segreta').lower().strip()
for x in range(100):
    print()
    digitadas = []
    acertos = []
    erros = 0
    tempo_inicial = time.time()
    while True:
        
        senha = ''
        for letra in palavra:
            senha += letra if letra in acertos else '-'
        print(senha)
        if senha == palavra:
            print('você acertou')
            tempo_final = time.time()
            tempo = tempo_final - tempo_inicial
            print(f'duração da partida {tempo:.2f}, você venceu')
            break 
        
        tentativas = input('\ndigite uma letra').lower().strip()
        if tentativas in digitadas:
            print('você ja tentou essa palavra')
            continue
        else:
            digitadas += tentativas
            if tentativas in palavra:
                acertos += tentativas
            else:
                erros += 1
                print('você errou')
            print('x==:==x\nx  :  ')
            print('x  o ' if erros >= 1 else 'x')    
            linha2 = ''
            if erros == 2:
                linha2 = ' | '
            elif erros == 3:
                linha3 = ' \| '
            elif erros >= 4:
                linha2 = ' \|/ '
            print(f'x{linha2}')
            linha3 = ''
            if erros == 5:
                linha3 +=  ' / '
            elif erros >= 6:
                linha3 += ' / \ '
            print(f'x{linha3}')
            if erros == 6:
                tempo_final = time.time()
                tempo = tempo_final - tempo_inicial
                print(f'enforcado!, duração {tempo}')
                break              