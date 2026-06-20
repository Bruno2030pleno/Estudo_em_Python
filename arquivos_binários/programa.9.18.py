# # programa # 9.18, viasualizador de arquivos em formatos binários 
# import sys
# import itertools

# def imprimir_bytes(imagem, bytes_por_linha=16):
#     for b in itertools.batched(imagem, bytes_por_linha):
#         hex_view = ' '.join([f"{v:02x}" for v in b])  # Adicionei um espaço para separar os hexadecimais
#         tvview = ''.join([chr(v) if 32 <= v <= 126 else "." for v in b]) # Garante caracteres imprimíveis ASCII
        
#         # Ajuste no espaçamento para alinhar o texto no final do arquivo
#         espacamento = " " * 3 * (bytes_por_linha - len(b))
#         print(f"{hex_view}{espacamento}  |{tvview}|")

# # O bloco principal deve ficar totalmente para fora da função (sem espaços no início)

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Uso: python nome_do_script.py caminho_do_arquivo.bin")
#         sys.exit(1)
        
#     with open(sys.argv[1], 'rb') as f:
#         imagem = f.read(2024)  # Lê os bytes do arquivo e salva na variável
    
#     imprimir_bytes(imagem)  # Passa a imagem como argumento para a função 




# import sys
# import itertools

# def imprimir_bytes(imagem, bytes_por_linha=16):
#     for b in itertools.batched(imagem, bytes_por_linha):
#         hex_view = ' '.join([f"{v:02x}" for v in b])
#         tvview = ''.join([chr(v) if 32 <= v <= 126 else "." for v in b])
        
#         # Alinhamento perfeito caso o arquivo tenha menos de 512 bytes
#         espacamento = " " * 3 * (bytes_por_linha - len(b))
#         print(f"{hex_view}{espacamento}  |{tvview}|")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Uso: python nome_do_script.py caminho_do_arquivo.bin")
#         sys.exit(1)
        
#     with open(sys.argv[1], 'rb') as f:
#         # MODIFICAÇÃO AQUI: Passamos o número 512 como argumento para o read()
#         imagem = f.read(512) 
    
#     imprimir_bytes(imagem)




# import argparse
# import sys
# import itertools

# def imprimir_bytes(imagem, bytes_por_linha):
#     for b in itertools.batched(imagem, bytes_por_linha):
#         hex_view = ' '.join([f"{v:02x}" for v in b])
#         tvview = ''.join([chr(v) if 32 <= v <= 126 else "." for v in b])
        
#         # Alinhamento dinâmico baseado no número de bytes por linha informado
#         espacamento = " " * 3 * (bytes_por_linha - len(b))
#         print(f"{hex_view}{espacamento}  |{tvview}|")

# if __name__ == "__main__":
#     # Configuração dos argumentos da linha de comando
#     parser = argparse.ArgumentParser(
#         description="Visualizador Hexadecimal customizável via terminal."
#     )
    
#     # Argumento obrigatório
#     parser.add_argument("arquivo", help="Caminho do arquivo a ser lido")
    
#     # Argumentos opcionais com valores padrão (default) caso o usuário não informe
#     parser.add_argument("-b", "--bytes", type=int, default=512, 
#                         help="Número máximo de bytes a ler (padrão: 512)")
#     parser.add_argument("-l", "--linhas", type=int, default=16, 
#                         help="Quantidade de bytes por linha (padrão: 16)")
    
#     args = parser.parse_args()

#     try:
#         with open(args.arquivo, 'rb') as f:
#             # Lê o número máximo de bytes especificado no argumento '--bytes'
#             imagem = f.read(args.bytes)
        
#         # Passa a imagem e a quantidade de bytes por linha para a função
#         imprimir_bytes(imagem, args.linhas)
        
#     except FileNotFoundError:
#         print(f"Erro: O arquivo '{args.arquivo}' não foi encontrado.")
#         sys.exit(1)


