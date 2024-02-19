from zz_filtragem import Filtragem

class Estudantes():
    global data 
    data = Filtragem.filtragem_serv_sociais()
    global todos_estudantes
    todos_estudantes = []
    global estudante_selecionado
    estudante_selecionado = []
    
    def __init__(self):
        pass

    def mdl_listar_estudantes():
        for estudante in data:
            todos_estudantes.append(estudante)
        return todos_estudantes
    
    def mdl_estudante_especifico(pegar_estudante):
        encontrado = False
        for estudante in data:
            if pegar_estudante == estudante["nome"] or pegar_estudante == str(estudante["id"]):
                estudante_selecionado.append(estudante)
                encontrado = True
                break
        if not encontrado:
            return encontrado
        return estudante_selecionado
