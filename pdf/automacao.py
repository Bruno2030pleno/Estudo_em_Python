import pdfplumber
import os
import sys


pasta_do_script = os.path.dirname(os.path.abspath(__file__))
arquivos_na_pasta = [f for f in os.listdir(pasta_do_script) if f.endswith('.pdf')]

if not arquivos_na_pasta:
    print(f"Erro: Não encontrei nenhum PDF em: {pasta_do_script}")
    sys.exit()

arquivo_pdf = os.path.join(pasta_do_script, arquivos_na_pasta[0])

def extrair_vias_texto(caminho_pdf):
    lista_itens = []
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto_completo = pdf.pages[0].extract_text()
            
            if texto_completo:
                linhas = texto_completo.split('\n')
                for linha in linhas:
                    partes = linha.split()
                    if len(partes) > 2 and partes[0].isdigit() and len(partes[0]) == 4:
                        lista_itens.append(partes)
        return lista_itens
    except Exception as e:
        print(f"Erro: {e}")
        return []


dados = extrair_vias_texto(arquivo_pdf)

if not dados:
    print("Aviso: Nenhum dado válido encontrado para gerar relatório.")
    sys.exit()

nome_saida = "relatorio_abril_2026.txt"
caminho_saida = os.path.join(pasta_do_script, nome_saida)

print(f"Arquivo lido: {os.path.basename(arquivo_pdf)}")
print(f"{'CÓDIGO':<8} | {'DESCRIÇÃO':<35} | {'VALOR':<10}")
print("-" * 60)

with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write("Relatório de Pagamento - José Bruno Nobre\n")
    f.write("-" * 50 + "\n")
    
    total_descontos = 0.0
    for item in dados:
        codigo = item[0]
        descricao = " ".join([p for p in item[1:] if not p.replace('.', '').replace(',', '').isdigit()])
        valor_str = item[-1].replace('.', '').replace(',', '.')
        
        try:
            valor_num = float(valor_str)
            
            if "DESC" in descricao or "EMPRESTIMO" in descricao:
                total_descontos += valor_num
                tipo = "DESCONTO"
            else:
                tipo = "PROVENTO"
                
            # Exibe na tela
            print(f"{codigo:<8} | {descricao[:35]:<35} | {valor_num:>10.2f} ({tipo})")
            
            # Salva no arquivo de texto ao mesmo tempo
            f.write(f"{codigo} | {descricao[:30]:<30} | R$ {valor_num:>8.2f}\n")
            
        except ValueError:
            continue

    print("-" * 60)
    print(f"Total de Descontos Calculado: R$ {total_descontos:.2f}")
    
    f.write("-" * 50 + "\n")
    f.write(f"Total de Descontos: R$ {total_descontos:.2f}\n")

print(f"\nSucesso! O arquivo '{nome_saida}' foi gerado em:\n{caminho_saida}")