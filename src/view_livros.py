from zz_linhas import linhas
class ViewLivros():
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
    
    def view_listar_livros_disponiveis(livros_disponiveis):
        linhas()
        for indice, livro in enumerate(livros_disponiveis):
            print(indice, ' - ',livro)
        linhas()
        while True:
            try:
                pegar_livro = int(input("Insira o índice da livro desejada: "))
                if pegar_livro < len(livros_disponiveis):
                    break
                else:
                    print("Índice inválido, tente novamente")
            except ValueError:
                print("Valor inválido, tente novamente")
        return pegar_livro
    
    def view_listar_livros_ja_reservados(livros):
        if len(livros) == 0:
            print("Nenhum livro reservado")
        else:
            linhas()
            print("Livros reservados:")
            for livro in livros:
                print(livro)
            linhas()
    
    def view_listar_livros_disponiveis_para_remocao(estudante):
        if len(estudante) == 0:
            return False
        else:
            linhas()
            for indice, livro in enumerate(estudante):
                print(indice, ' - ',livro)
            linhas()
            while True:
                try:
                    pegar_livro = int(input("Insira o índice da livro desejada: "))
                    if pegar_livro < len(estudante):
                        break
                    else:
                        print("Índice inválido, tente novamente")
                except ValueError:
                    print("Valor inválido, tente novamente")
            return pegar_livro
    
    def view_nao_encontrou():
        linhas()
        print("Estudante não encontrado")
        linhas()
    
    def view_adicionou():
        linhas()
        print("Livro reservado com sucesso")
        linhas()

    def view_ja_reservado():
        linhas()
        print("Livro já reservado")
        linhas()
    
    def view_removeu():
        linhas()
        print("Livro devolvido com sucesso")
        linhas()

    def view_aluno_vazio():
        linhas()
        print("O aluno não reservou um livro ainda")
        linhas()

    def view_vazio():
        linhas()
        print("Nenhum aluno reservou um livro ainda")
        linhas()