"""
Faça uma lista de tarefas com as seguintes opcoes:
    - adicionar tarefa
    - listar tarefas
    - opcao de desfazer (a cada vez que chamarmos, desfaz a ultima acao)
    - opcao de refazer (a cada vez que chamarmos, refaz a ultima acao)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] < - Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer

"""


#
#
# def menu():
#     print("Menu:")
#     print('\t1- Adicionar Tarefa.')
#     print('\t2- Listar Tarefas.')
#     print('\t3- Desfazer.')
#     print('\t4- Refazer.')
#     print('\t5- Sair.')
#     print('\t6 - print.')
#     opcao = input('Opcao: ')
#     print('\n')
#     return opcao
#
#
# def listar_tarefa(lista):
#     if lista is None or lista == []:
#         print('Não possui tarefas.')
#     else:
#         for k, tarefa in enumerate(lista):
#             print(f'Tarefa {k + 1}')
#             print(f'\t{tarefa}')
#
#
# def remover_tarefa(lista_de_tarefa, ultima_tarefa=None):
#     if lista_de_tarefa is None or lista_de_tarefa == []:
#         print('Não foi possivel remover.')
#     else:
#         if ultima_tarefa is None or ultima_tarefa == []:
#             ultima_tarefa = []
#         ultima_tarefa.append(lista_de_tarefa[-1])
#         ultima = ultima_tarefa[-1]
#         lista_de_tarefa.pop()
#         print(f'A tarefa "{ultima}" foi removida.')
#     return lista_de_tarefa, ultima_tarefa
#
#
# def refazer_tarefa(lista_de_tarefa, tarefa=None):
#     if tarefa is None or tarefa == []:
#         print('Não foi possivel refazer a ultima tarefa.')
#     else:
#         lista_de_tarefa.append(tarefa[-1])
#         print(f'A tarefa "{tarefa[-1]}" foi refeita.')
#         tarefa.pop()
#     return lista_de_tarefa, tarefa
#
#
# def adicionar_tarefa(lista, ultima_tarefa):
#     tarefa = input('Digite o nome da tarefa: ')
#     if lista is None:
#         lista = []
#     ultima_tarefa = []
#     lista.append(tarefa)
#     return lista, ultima_tarefa
#
#
# lista_de_tarefa = []
# ultima_tarefa = []
#
# while 1:
#     opcao = menu()
#
#     if opcao.isnumeric():
#         opcao = int(opcao)
#     else:
#         print('Insira uma opcao válida')
#     if opcao == 5:
#         break
#     elif opcao == 1:
#         lista_de_tarefa, ultima_tarefa = adicionar_tarefa(lista_de_tarefa, ultima_tarefa)
#     elif opcao == 2:
#         listar_tarefa(lista_de_tarefa)
#     elif opcao == 3:
#         lista_de_tarefa, ultima_tarefa = remover_tarefa(lista_de_tarefa, ultima_tarefa)
#     elif opcao == 4:
#         lista_de_tarefa, ultima_tarefa = refazer_tarefa(lista_de_tarefa, ultima_tarefa)
#     elif opcao == 6:
#         print(lista_de_tarefa)
#         print(ultima_tarefa)
#     else:
#         print('Digite uma opção valida.')
#
#
#
#
#
#

def do_menu():
    print("Menu:")
    print('\t1 - Adicionar Tarefa.')
    print('\t2 - Listar Tarefas.')
    print('\t3 - Desfazer.')
    print('\t4 - Refazer.')
    print('\t5 - Sair.')
    print('\t6 - Print.')
    opcao = input('Opção: ')
    print('\n')
    return opcao


def do_list(todo_list):
    if todo_list is None or todo_list == []:
        print('Não possui tarefas.')
    else:
        for k, tarefa in enumerate(todo_list):
            print(f'Tarefa {k + 1}')
            print(f'\t{tarefa}')


def do_undo(todo_list, last_list=None):
    if todo_list is None or todo_list == []:
        print('Não foi encontrada tarefas para remover.')
    else:
        if last_list is None or last_list == []:
            last_list = []
        print(f'A tarefa "{todo_list[-1]}" foi removida.')
        last_list.append(todo_list.pop())
    return todo_list, last_list


def do_redo(todo_list, last_list=None):
    if last_list is None or last_list == []:
        print('Não foi possivel refazer a ultima tarefa.')
    else:
        print(f'A tarefa "{last_list[-1]}" foi refeita.')
        todo_list.append(last_list.pop())
    return todo_list, last_list


def do_add(todo_list, last_list):
    if todo_list is None:
        todo_list = []
    last_list = []
    tarefa = input('Digite o nome da tarefa: ')
    todo_list.append(tarefa)
    return todo_list, last_list


if __name__ == '__main__':
    todo_list = []
    last_list = []

    while 1:
        opcao = do_menu()

        if opcao.isnumeric():
            opcao = int(opcao)
        else:
            print('Insira uma opção válida')
            continue
        if opcao == 5:
            break
        elif opcao == 1:
            todo_list, last_list = do_add(todo_list, last_list)
        elif opcao == 2:
            do_list(todo_list)
        elif opcao == 3:
            todo_list, last_list = do_undo(todo_list, last_list)
        elif opcao == 4:
            todo_list, last_list = do_redo(todo_list, last_list)
        elif opcao == 6:
            print(todo_list)
            print(last_list)
        else:
            print('Digite uma opção valida.')
