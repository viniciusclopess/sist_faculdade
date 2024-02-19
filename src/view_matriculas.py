from zz_linhas import linhas
class ViewMatriculas():
    def __init__(self):
        pass

    def view_pegar_nome_estudante():
        while True:
            pegar_estudante = input("Insira o nome ou ID do estudante: ")
            if pegar_estudante != '':
                break
            else:
                print("Algo deu errado, tente novamente")  
        return pegar_estudante

    def view_listar_disciplinas_disponiveis(disciplinas_disponiveis):
        linhas()
        for indice, disciplina in enumerate(disciplinas_disponiveis):
            print(indice, ' - ',disciplina)
        linhas()
        while True:
            try:
                pegar_disciplina = int(input("Insira o índice da disciplina desejada: "))
                if pegar_disciplina < len(disciplinas_disponiveis):
                    break
                else:
                    print("Índice inválido, tente novamente")
            except ValueError:
                print("Valor inválido, tente novamente")
        return pegar_disciplina
    
    def view_listar_disciplinas_ja_matriculadas(matriculas):    
        if len(matriculas) == 0:
            print("Nenhuma disciplina matriculada")
        else:
            linhas()
            print("Disciplinas matriculadas:")
            for matricula in matriculas:
                print(matricula)
            linhas()
    
    def view_listar_disciplinas_disponiveis_para_remocao(estudante):
        if len(estudante) == 0:
            return False
        else:
            linhas()
            for indice, disciplina in enumerate(estudante):
                print(indice, ' - ',disciplina)
            linhas()
            while True:
                try:
                    pegar_disciplina = int(input("Insira o índice da disciplina desejada: "))
                    if pegar_disciplina < len(estudante):
                        break
                    else:
                        print("Índice inválido, tente novamente")
                except ValueError:
                    print("Valor inválido, tente novamente")
            return pegar_disciplina
    
    def view_nao_encontrou():
        linhas()
        print("Estudante não encontrado")
        linhas()
    
    def view_adicionou():
        linhas()
        print("Disciplina adicionada com sucesso")
        linhas()
    
    def view_ja_matriculado():
        linhas()
        print("Estudante já matriculado nesta disciplina")
        linhas()

    def view_removeu():
        linhas()
        print("Disciplina removida com sucesso")
        linhas()
    
    def view_aluno_vazio():
        linhas()
        print("Nenhum aluno se matriculou ainda")
        linhas()
        
    def view_vazio():
        linhas()
        print("Nenhum aluno se matriculou ainda")
        linhas()
            