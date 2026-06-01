import PyPDF2
from deep_translator import GoogleTranslator
import os # Biblioteca nativa adicionada para lidar com caminhos de arquivos

def traduzir_pdf(caminho_pdf_entrada, caminho_txt_saida):
    print("--- Iniciando a leitura do PDF ---")
    
    try:
        with open(caminho_pdf_entrada, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            total_paginas = len(leitor_pdf.pages)
            print(f"O PDF tem {total_paginas} página(s).")

            with open(caminho_txt_saida, 'w', encoding='utf-8') as arquivo_saida:
                tradutor = GoogleTranslator(source='en', target='pt')

                for numero_pagina in range(total_paginas):
                    print(f"Processando página {numero_pagina + 1}...")
                    
                    pagina = leitor_pdf.pages[numero_pagina]
                    texto_original = pagina.extract_text()
                    
                    if texto_original:
                        texto_traduzido = tradutor.translate(texto_original)
                        arquivo_saida.write(f"--- PÁGINA {numero_pagina + 1} ---\n")
                        arquivo_saida.write(texto_traduzido + "\n\n")
                    else:
                        arquivo_saida.write(f"--- PÁGINA {numero_pagina + 1} VAZIA OU ILEGÍVEL ---\n\n")

            print(f"\nSucesso! A tradução foi salva no arquivo: {caminho_txt_saida}")
            
    except FileNotFoundError:
        print(f"\nErro: O arquivo não foi encontrado.")
        print(f"O Python procurou exatamente neste endereço:\n{caminho_pdf_entrada}")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")


# --- O TRUQUE PARA NUNCA MAIS DAR ERRO DE PASTA ---

# 1. O Python descobre automaticamente o caminho absoluto da pasta onde este código está salvo
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# 2. Ele junta a pasta certa com os nomes dos arquivos
pdf_em_ingles = os.path.join(pasta_atual, "t.pdf")
txt_em_portugues = os.path.join(pasta_atual, "traducao_final.txt")

# Roda o script com os caminhos absolutos gerados automaticamente
traduzir_pdf(pdf_em_ingles, txt_em_portugues)