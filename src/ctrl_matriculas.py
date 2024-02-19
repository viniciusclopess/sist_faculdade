from mdl_matriculas import Matriculas
from view_matriculas import ViewMatriculas
class CtrlMatriculas():
    global data_matriculas
    data_matriculas = Matriculas.mdl_dados_disciplinas()
    global i 
    i = 0

    def __init__(self):
        pass

    @staticmethod
    def ctrl_listar_disciplinas():
        pegar_estudante = ViewMatriculas.view_pegar_nome_estudante()
        listagem = Matriculas.mdl_listar_disciplinas_matriculadas(pegar_estudante, data_matriculas)
        ViewMatriculas.view_listar_disciplinas_ja_matriculadas(listagem)

    @staticmethod
    def ctrl_adicionar_disciplinas():
        global i, data_matriculas
        if i == 0:
            data_matriculas = Matriculas.mdl_dados_disciplinas()
            pegar_estudante = ViewMatriculas.view_pegar_nome_estudante()
            pegar_disciplinas_disponiveis = Matriculas.mdl_disciplinas_disponiveis()
            listar_disciplinas_disponiveis = ViewMatriculas.view_listar_disciplinas_disponiveis(pegar_disciplinas_disponiveis)
            data_matriculas = Matriculas.mdl_adicionar_matriculas(pegar_estudante, listar_disciplinas_disponiveis, data_matriculas)
            if type(data_matriculas) == bool:
                ViewMatriculas.view_nao_encontrou()
            else:
                ViewMatriculas.view_adicionou()
                Matriculas.mdl_atualizar_dados_disciplinas(data_matriculas)
                i += 1
        else:
            pegar_estudante = ViewMatriculas.view_pegar_nome_estudante()
            pegar_disciplinas_disponiveis = Matriculas.mdl_disciplinas_disponiveis()
            listar_disciplinas_disponiveis = ViewMatriculas.view_listar_disciplinas_disponiveis(pegar_disciplinas_disponiveis)
            auxiliar = data_matriculas
            data_matriculas = Matriculas.mdl_adicionar_matriculas(pegar_estudante, listar_disciplinas_disponiveis, data_matriculas)
            if type(data_matriculas) == bool:
                ViewMatriculas.view_nao_encontrou()
            elif type(data_matriculas) == int:
                ViewMatriculas.view_ja_matriculado()
                data_matriculas = auxiliar
            else:
                ViewMatriculas.view_adicionou()
                Matriculas.mdl_atualizar_dados_disciplinas(data_matriculas)

    @staticmethod
    def ctrl_remover_disciplinas():
        global i, data_matriculas
        if i == 0:
            ViewMatriculas.view_vazio()
        else:
            pegar_estudante = ViewMatriculas.view_pegar_nome_estudante()
            pegar_disciplinas_estudante = Matriculas.mdl_pegar_estudante(pegar_estudante, data_matriculas)
            listar_disciplinas_estudante = ViewMatriculas.view_listar_disciplinas_disponiveis_para_remocao(pegar_disciplinas_estudante)
            if listar_disciplinas_estudante == False:
                ViewMatriculas.view_aluno_vazio()
            else:
                auxiliar = data_matriculas
                data_matriculas = Matriculas.mdl_remover_matriculas(pegar_estudante, listar_disciplinas_estudante, data_matriculas)
                if type(data_matriculas) == bool:
                    ViewMatriculas.view_nao_encontrou()
                elif type(data_matriculas) == int:
                    ViewMatriculas.view_ja_matriculado()
                    data_matriculas = auxiliar
                else:
                    ViewMatriculas.view_removeu()
                    Matriculas.mdl_atualizar_dados_disciplinas(data_matriculas)
