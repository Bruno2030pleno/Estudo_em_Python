import sys
import os

def linha_de_comando():
    # 1. VALIDAÇÃO DE ARGUMENTOS: Verifica se o usuário passou os 3 parâmetros necessários
    # O len(sys.argv) deve ser 4 (nome_do_script + arquivo + inicio + fim)
    if len(sys.argv) < 4:
        print("ERRO: Você precisa passar o nome do arquivo, a linha inicial e a final.")
        print("Uso: python exercicio_9.13__.py <arquivo.txt> <inicio> <fim>")
        return 

    # 2. ATRIBUIÇÃO DE VARIÁVEIS: Agora que sabemos que os dados existem, nós os capturamos
    nome_1 = sys.argv[1]
    
    try:
        nome_2 = int(sys.argv[2])
        nome_3 = int(sys.argv[3])
    except ValueError:
        print("ERRO: A linha inicial e a final devem ser números inteiros.")
        return

    # 3. VALIDAÇÃO DE EXISTÊNCIA: Verifica se o arquivo físico realmente está na pasta
    if not os.path.exists(nome_1):
        print(f"ERRO: O arquivo '{nome_1}' não foi encontrado nesta pasta.")
        return

    # 4. PROCESSAMENTO DO ARQUIVO
    try:
        with open(nome_1, 'r', encoding='utf-8') as novo_arquivo:
            metado = novo_arquivo.readlines()
            
            # Fatiamento ajustado (nome_2 - 1 para alinhar com o índice 0 do Python)
            selecao = metado[nome_2 - 1 : nome_3]
            
            # 5. EXIBIÇÃO DOS RESULTADOS
            if not selecao:
                print("Aviso: O intervalo selecionado está fora do alcance das linhas do arquivo.")
            else:
                for linha in selecao:
                    print(linha, end='')
                    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# CHAMADA DA FUNÇÃO
if __name__ == "__main__":
    linha_de_comando()


        