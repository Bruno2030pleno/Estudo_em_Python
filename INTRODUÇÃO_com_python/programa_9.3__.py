# geração de numeros pares e impares em arquivos diferentes

with open('impares.txt', 'w') as impares:
    with open('ipar.txt', 'w') as ipas:
        for n in range(1, 1000):
            if n % 2 == 0:
                ipas.write(f'{n}\n')
            else:
                impares.write(f"{n}\n")

# with open('ipar.txt', 'w') as ipas, open('impares.txt', 'w') as impares:
#     for n in range(1, 1000):
#         if n % 2 == 0:
#             ipas.write(f'{n}\n')
#         else:
#             impares.write(f"{n}\n")

# filtrar 
# Primeiro, lemos o arquivo de origem ('r')
# Depois, criamos o arquivo de destino ('w')
# with open('pares.txt', 'r') as pares, open('multiplos de 4.txt', 'w') as multiplas4:
#     for linha in pares:
#         # O strip() remove espaços e quebras de linha (\n) para evitar erros na conversão
#         numero = int(linha.strip())
        
#         if numero % 4 == 0:
#             # Escrevemos o número de volta com uma quebra de linha
#             multiplas4.write(f"{numero}\n")