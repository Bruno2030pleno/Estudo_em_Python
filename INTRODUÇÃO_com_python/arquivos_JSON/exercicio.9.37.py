# escreva um programa que leia o nome do aluno
# e quatro notas no final
# o programa deve gravar os dados lidos em um arquivo em disco
# usando o formato JSON 
import json
from pathlib import Path

def criando_arquivo_json():
    # 1. Coleta e estrutura dos dados
    nome_aluno = input("Digite o nome do aluno: ")
    materias = ["Matemática", "Inglês", "Português", "Ciências"]
    notas = []
    
    # Loop para ler as 4 notas
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    dados_aluno = {
        "nome": nome_aluno,
        "materias": materias,
        "notas": notas
    }

    # 2. Gravando no arquivo
    caminho = Path("notas_do_aluno.json")
    caminho.write_text(json.dumps(dados_aluno, indent=4, ensure_ascii=False), encoding="utf-8")
    print("\nDados gravados com sucesso!\n")

    # 3. Lendo do arquivo
    conteudo = caminho.read_text(encoding="utf-8")
    dados = json.loads(conteudo)

    # 4. Exibindo os dados (sem o erro de loop desnecessário)
    print(f"Nome do aluno: {dados['nome']}")
    print(f"Matérias: {', '.join(dados['materias'])}")
    print(f"Notas: {dados['notas']}")
    
    media = sum(dados['notas']) / len(dados['notas'])
    print(f"Média final: {media:.2f}")

criando_arquivo_json()      