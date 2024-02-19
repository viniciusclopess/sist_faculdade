from zz_linhas import linhas
class ViewEstudantes:
    def __init__(self):
        pass

    def view_pegar_estudante():
        pegar_estudante = input("Insira o nome ou ID do estudante: ")
        return pegar_estudante
    
    def view_listar_estudantes(todos_estudantes):
        linhas()
        i = 0
        for estudante in todos_estudantes:
            print(estudante['nome'])
            print(estudante['id'])
            print(estudante['curso'])
            linhas()

    def view_estudante_especifico(estudante_selecionado):
        linhas()
        for estudante in estudante_selecionado:
            print(estudante['nome'])
            print(estudante['id'])
            print(estudante['curso'])
            linhas()
    
    def view_deu_ruim():
        linhas()
        print("Estudante não encontrado")
        linhas()
            