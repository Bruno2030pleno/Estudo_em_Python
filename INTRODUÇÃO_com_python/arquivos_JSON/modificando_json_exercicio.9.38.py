# modifique o programa anterior para que leia o mesmo arquivo,
# permindo adicionar mais dados ao arquivo !!!!!. se o mesmo nome for digitado
# duas vezes altere os dados para a nova entrada!!!!!!
import json
from pathlib import Path
def modificar_notas():
    caminho = Path('notas_do_aluno.json')
    # Carrega os dados existentes (ou começa vazio se o arquivo não existir)
    if caminho.exists():
        dados = json.loads(caminho.read_text(encoding='utf-8'))
    else:
        dados = {}
    print('=== Adicionar / Atualizar Notas ===')
    print('Digite o nome em branco para terminar\n')
    while True:
        nome = input('Nome do aluno: ').strip()
        if not nome:  # se digitar enter sem nome, encerra
            break
        # Avisa se o aluno já existe (vai atualizar)
        if nome in dados:
            print(f'"{nome}" já existe com nota {dados[nome]}. A nota será atualizada.')
        nota = input(f'Nota de {nome}: ').strip()
        dados[nome] = nota
        # Salva imediatamente após cada entrada
        caminho.write_text(json.dumps(dados, indent=4, ensure_ascii=False), encoding='utf-8')
        print(f'"{nome}" salvo com sucesso!\n')
    print('\n=== Notas registradas ===')
    for aluno, nota in dados.items():
        print(f'{aluno}: {nota}')
modificar_notas()