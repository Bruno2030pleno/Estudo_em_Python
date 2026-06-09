import PyPDF2
import os

def  ler():
    print('leitura com sucesso')
    arquivo = 'arquivob.pdf'
    
    if not os.path.exists(arquivo):
        print('arquivo nao existe')
        return

    
    with open(arquivo, 'rb') as leitura:
       pdf_leitura = PyPDF2.PdfReader(leitura)
       for m, n in enumerate(pdf_leitura.pages):
           t = n.extract_text()
           print(f"\n--- Lendo a Página {m + 1} ---")
           print(t)      
ler()           