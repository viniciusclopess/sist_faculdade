from mdl_estudantes import Estudantes
from view_estudantes import ViewEstudantes
class CtrlEstudantes:
    def __init__(self):
        pass

    @staticmethod 
    def crtl_listar_estudantes():
        todos_estudantes = Estudantes.mdl_listar_estudantes()
        ViewEstudantes.view_listar_estudantes(todos_estudantes)
    
    @staticmethod
    def ctrl_estudante_especifico():
        pegar_estudante = ViewEstudantes.view_pegar_estudante()
        estudante_selecionado = Estudantes.mdl_estudante_especifico(pegar_estudante)
        if type(estudante_selecionado) == bool:
            ViewEstudantes.view_deu_ruim()
        else:
            ViewEstudantes.view_estudante_especifico(estudante_selecionado)  
        