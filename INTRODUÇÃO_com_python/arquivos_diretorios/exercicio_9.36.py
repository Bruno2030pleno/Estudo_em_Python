# exercicio utilizando a função os.walk. crie um programa que calcule
# o espaço ocupado por diretorios e subdiretorios, gerando uma página HTML
# com os resultados

import os
import sys

# PASSO 1: Verifique se o diretório foi passado na linha de comando (sys.argv)
# e guarde-o em uma variável (ex: diretorio_alvo).

# PASSO 2: Abra um arquivo HTML para escrita (ex: 'tamanho_diretorios.html' com modo 'w').
# Escreva o cabeçalho básico do HTML (<html>, <body>, <h1>, etc).

# PASSO 3: Inicie o laço for principal usando os.walk(diretorio_alvo).
# Lembre-se: ele retorna raiz, diretorios, arquivos.

# PASSO 4: DENTRO do laço do os.walk, crie uma variável "tamanho_total_dir" iniciando em 0.
# Faça um laço interno nos "arquivos", pegue o caminho completo de cada um,
# use os.path.getsize() e SOME esse valor na variável "tamanho_total_dir".

# PASSO 5: Ainda DENTRO do laço do os.walk (mas fora do laço dos arquivos),
# escreva no HTML uma linha mostrando o nome do diretório (a "raiz") e o seu tamanho total.

# PASSO 6: Feche as tags HTML no final de tudo.

if len(sys.argv) < 2:
    print('você precisa passar um arquivo e um caminho')
    sys.exit()

diretorio_alvo = sys.argv[1]  # 
arquivo_saida = 'site_simples.html'

with open(arquivo_saida, 'w', encoding='utf-8') as pagina:
    pagina.write("<!DOCTYPE html>\n<html>\n<head><meta charset='UTF-8'></head>\n<body>\n")
    pagina.write("<h1>Relatório de Arquivos</h1>\n<ul>\n")
    
    for raiz, diretorio, arquivos in os.walk(diretorio_alvo):
        tamanho_total_dir = 0  # PASSO 4: Inicia a soma zerada para ESTE diretório
        
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)    
            try:
                tamanho_total_dir += os.path.getsize(caminho_completo)  # Soma o tamanho do arquivo ao total do diretório
            except OSError as e:
                print(f"Não foi possível ler {nome_arquivo}: {e}")
                
        # PASSO 5: Escreve o resultado do DIRETÓRIO (fora do laço dos arquivos)
        pagina.write(f"<li>Diretório: <b>{raiz}</b> - Tamanho Total: {tamanho_total_dir} bytes</li>\n")
        
    # PASSO 6: Fechamento do HTML fora de todos os laços
    pagina.write("</ul>\n</body>\n</html>\n")

print(f"Relatório gerado com sucesso: {arquivo_saida}")       