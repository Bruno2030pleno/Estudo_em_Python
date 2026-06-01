def listar(tarefas):
    if not tarefas:
        print('nao ha tarefas para listar ')
        return
    
    print('tarefas')
    for tarefa in tarefas:
        print(tarefa)

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('nao ha tarefas para desfazer ')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('nao ha tarefas para refazer ')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('nao ha tarefas para executar ')
        return
    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []  


while True:
    listar_tarefa = input('digite uma tarefa ou l (listar) : d (desfazer) : r (refazer): ') 
    if listar_tarefa == 'l':
        listar(tarefas)
        continue       
    elif listar_tarefa == 'd':
        desfazer(tarefas,tarefas_refazer) 
        continue
    elif listar_tarefa == 'r':
        refazer(tarefas, tarefas_refazer)
        continue
    else:
        adicionar(listar_tarefa, tarefas)
       
