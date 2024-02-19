from ctrl_estudantes import CtrlEstudantes
from ctrl_matriculas import CtrlMatriculas
from ctrl_livros import CtrlLivros
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')   

while True:
    clear_terminal()
    print('1 - Estudantes')
    print('2 - Disciplinas')
    print('3 - Livros')
    print('4 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        clear_terminal()
        print('1 - Listar estudantes')
        print('2 - Buscar estudante específico')
        print('3 - Sair')
        opcao = input('Digite a opção desejada: ')
        clear_terminal()
        if opcao == '1':
            CtrlEstudantes.crtl_listar_estudantes()
            input('Pressione enter para continuar...')
        elif opcao == '2':
            CtrlEstudantes.ctrl_estudante_especifico()
            input('Pressione enter para continuar...')
        elif opcao == '3':
            break
    elif opcao == '2':
        clear_terminal()
        print('1 - Listar disciplinas matriculadas')
        print('2 - Adicionar disciplinas')
        print('3 - Remover disciplinas')
        print('4 - Sair')
        opcao = input('Digite a opção desejada: ')
        clear_terminal()
        if opcao == '1':
            CtrlMatriculas.ctrl_listar_disciplinas()
            input('Pressione enter para continuar...')
        elif opcao == '2':
            CtrlMatriculas.ctrl_adicionar_disciplinas()
            input('Pressione enter para continuar...')
        elif opcao == '3':
            CtrlMatriculas.ctrl_remover_disciplinas()
            input('Pressione enter para continuar...')
        elif opcao == '4':
            break
    elif opcao == '3':
        clear_terminal()
        print('1 - Listar livros reservados')
        print('2 - Adicionar livros')
        print('3 - Remover livros')
        print('4 - Sair')
        opcao = input('Digite a opção desejada: ')
        clear_terminal()
        if opcao == '1':
            CtrlLivros.ctrl_listar_livros()
            input('Pressione enter para continuar...')
        elif opcao == '2':
            CtrlLivros.ctrl_adicionar_livros()
            input('Pressione enter para continuar...')
        elif opcao == '3':
            CtrlLivros.ctrl_remover_livros()
            input('Pressione enter para continuar...')
        elif opcao == '4':
            break
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
        continue