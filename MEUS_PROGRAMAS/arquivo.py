import sys
# 1. Primeiro verificamos se o argumento foi passado na linha de comando

if len(sys.argv) < 2:
    print('Erro: Você precisa informar o nome do arquivo.')
    sys.exit()

arquivo_beta = sys.argv[1] # 2. Pegamos o nome do arquivo passado no terminal (ex: lembrete.txt)
lista_de_nomes = ['python', 'java', 'c', 'javascript']

with open(arquivo_beta, 'w', encoding='utf-8') as teste:
    for nomes in lista_de_nomes:
        teste.write(f'{nomes}\n')
print(f'Arquivo "{arquivo_beta}" gerado com sucesso!')





      