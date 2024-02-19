from mdl_livros import Livros
from view_livros import ViewLivros
class CtrlLivros():
    global data_livros
    data_livros = Livros.mdl_dados_livros()
    global i 
    i = 0

    def __init__(self):
        pass

    @staticmethod
    def ctrl_listar_livros():
        pegar_estudante = ViewLivros.view_pegar_nome_estudante()
        listagem = Livros.mdl_listar_livros_reservados(pegar_estudante, data_livros)
        ViewLivros.view_listar_livros_ja_reservados(listagem)

    @staticmethod
    def ctrl_adicionar_livros():
        global i, data_livros
        if i == 0:
            data_livros = Livros.mdl_dados_livros()
            pegar_estudante = ViewLivros.view_pegar_nome_estudante()
            pegar_livros_disponiveis = Livros.mdl_livros_disponiveis()
            listar_livros_disponiveis = ViewLivros.view_listar_livros_disponiveis(pegar_livros_disponiveis)
            data_livros = Livros.mdl_adicionar_livros(pegar_estudante, listar_livros_disponiveis, data_livros)
            if type(data_livros) == bool:
                ViewLivros.view_nao_encontrou()
            else:
                ViewLivros.view_adicionou()
                Livros.mdl_atualizar_dados_livros(data_livros)
                i += 1
        else:
            pegar_estudante = ViewLivros.view_pegar_nome_estudante()
            pegar_livros_disponiveis = Livros.mdl_livros_disponiveis()
            listar_livros_disponiveis = ViewLivros.view_listar_livros_disponiveis(pegar_livros_disponiveis)
            auxiliar = data_livros
            data_livros = Livros.mdl_adicionar_livros(pegar_estudante, listar_livros_disponiveis, data_livros)
            if type(data_livros) == bool:
                ViewLivros.view_nao_encontrou()
            elif type(data_livros) == int:
                ViewLivros.view_ja_matriculado()
                data_livros = auxiliar
            else:
                ViewLivros.view_adicionou()
                Livros.mdl_atualizar_dados_livros(data_livros)

    @staticmethod
    def ctrl_remover_livros():
            global i, data_livros
            if i == 0:
                ViewLivros.view_vazio()
            else:
                pegar_estudante = ViewLivros.view_pegar_nome_estudante()
                pegar_livros_estudante = Livros.mdl_pegar_estudante(pegar_estudante, data_livros)
                listar_livros_estudante = ViewLivros.view_listar_livros_disponiveis_para_remocao(pegar_livros_estudante)
                if listar_livros_estudante == False:
                    ViewLivros.view_aluno_vazio()
                else:
                    auxiliar = data_livros
                    data_livros = Livros.mdl_remover_livros(pegar_estudante, listar_livros_estudante, data_livros)
                    if type(data_livros) == bool:
                        ViewLivros.view_nao_encontrou()
                    elif type(data_livros) == int:
                        ViewLivros.view_ja_reservado()
                        data_livros = auxiliar
                    else:
                        ViewLivros.view_removeu()
                        Livros.mdl_atualizar_dados_livros(data_livros)