# crei um programa que gere uma pagina html com links para todos os arquivos
# jpg e png econtradas a partir de um diretorio informado na linha comando

import sys
import os

if len(sys.argv) < 2:
    print('Erro: python3 exercicio_9.33__.py <caminho_do_diretorio>')
    
else: 
    diretorio_alvo = sys.argv[1]   
    
    # isdir já verifica se existe e se é de fato um diretório
    if os.path.isdir(diretorio_alvo):
        print(f'O diretório "{diretorio_alvo}" foi encontrado.')
        imagens_encontradas = []
        
        # Varrendo o diretório (corrigido: os.listdir)
        for nome_arquivo in os.listdir(diretorio_alvo):
            # Passamos os dois parâmetros para o join: a pasta e o arquivo
            caminho_completo = os.path.join(diretorio_alvo, nome_arquivo)
            
            # Verifica se é um arquivo e se termina com .jpg ou .png
            if os.path.isfile(caminho_completo) and nome_arquivo.lower().endswith(('.jpg', '.png')):
                imagens_encontradas.append(caminho_completo)
        
        # Gerando o arquivo HTML se imagens foram encontradas
        if imagens_encontradas:
            nome_html = 'galeria.html'
            with open(nome_html, 'w', encoding='utf-8') as pagina:
                pagina.write('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n')
                pagina.write('<meta charset="UTF-8">\n<title>Galeria de Imagens</title>\n</head>\n<body>\n')
                pagina.write('<h1>Imagens Encontradas</h1>\n<ul>\n')
                for img in imagens_encontradas:
                    # Cria o link HTML. os.path.basename pega só o nome do arquivo para exibir no texto
                    pagina.write(f'  <li><a href="{img}">{os.path.basename(img)}</a></li>\n')
                pagina.write('</ul>\n</body>\n</html>\n')
            print(f'Página "{nome_html}" gerada com sucesso com {len(imagens_encontradas)} imagem(ns)!')
        else:
            print('Nenhuma imagem .jpg ou .png foi encontrada neste diretório.')
    else:
        print('Erro: O diretório informado não existe ou não é uma pasta válida.')