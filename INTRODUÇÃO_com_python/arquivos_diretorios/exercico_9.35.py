# exercicio utilizando a função os.walk, crie uma pagina HTML
# com o nome e tamanho de cada arquivo de um diretorio passado e de seus subdiretorios

import os
import sys

# 1. Verifique se o caminho do diretório foi passado via terminal (usando sys.argv)
# 2. Abra um arquivo (ex: 'relatorio_arquivos.html') em modo de escrita ('w')
# 3. Escreva a estrutura básica inicial do HTML (<html>, <head>, <body>, e talvez iniciar uma <ul> ou <table>)
# 4. Crie o laço for com os.walk() passando o diretório alvo
# 5. Dentro do laço, passeie pelos arquivos e obtenha o tamanho de cada um
# 6. Escreva no arquivo HTML os dados (nome e tamanho) formatados
# 7. Após terminar os laços, escreva o fechamento das tags HTML (</body>, </html>)

import sys
import os

# 1. Validação dos argumentos
if len(sys.argv) < 2:
    print('Erro: está faltando o diretório alvo!')
    print('Uso: python3 nome_do_arquivo.py /caminho/do/diretorio')
    sys.exit(1)

diretorio_alvo = sys.argv[1]
arquivo_saida = 'site_simples.html'

# 2. Criação do arquivo HTML
with open(arquivo_saida, 'w', encoding='utf-8') as pagina:
    pagina.write("<!DOCTYPE html>\n<html>\n<head><meta charset='UTF-8'></head>\n<body>\n")
    pagina.write("<h1>Relatório de Arquivos</h1>\n<ul>\n")
    
    # 3. Varredura do diretório
    for raiz, diretorios, arquivos in os.walk(diretorio_alvo):
        for nome_do_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_do_arquivo)
            
            # Tratamento de erro caso o arquivo não possa ser lido
            try:
                tamanho = os.path.getsize(caminho_completo)
                pagina.write(f"<li>Arquivo: {nome_do_arquivo} - Tamanho: {tamanho} bytes</li>\n")
            except OSError as e:
                print(f"Não foi possível ler {nome_do_arquivo}: {e}")
            
    pagina.write("</ul>\n</body>\n</html>")

print(f"Relatório gerado com sucesso: {arquivo_saida}")
