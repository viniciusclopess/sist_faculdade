from zz_filtragem import Filtragem
class Matriculas():
    global data
    data = Filtragem.filtragem_serv_sociais()
    global lista_disciplinas
    lista_disciplinas = []
    global aux_adicionar
    aux_adicionar = []
    global disciplinas_disponiveis
    disciplinas_disponiveis = ['Introdução ao Serviço Social', 
    'Psicologia Social',
    'Serviço Social, Direito e Cidadania',
    'Sociologia Geral',
    'Fundamentos Históricos e Teórico-Metodológicos do Serviço Social I',]
    
    def __init__(self):
        pass

    def mdl_dados_disciplinas():
        data_matriculas = data
        nova_chave = 'matricula'
        for dicionario in data_matriculas:
            dicionario[nova_chave] = []
        return data_matriculas
    
    def mdl_atualizar_dados_disciplinas(data_matriculas):
        global data
        data = data_matriculas
        return data
    
    def mdl_disciplinas_disponiveis():
        disciplinas_disponiveis = ['Introdução ao Serviço Social', 
    'Psicologia Social',
    'Serviço Social, Direito e Cidadania',
    'Sociologia Geral',
    'Fundamentos Históricos e Teórico-Metodológicos do Serviço Social I',]
        return disciplinas_disponiveis
    
    def mdl_listar_disciplinas_matriculadas(nome_estudante, data_matriculas):
            for estudante in data_matriculas:
                if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                    lista_disciplinas = estudante['matricula']
                    return lista_disciplinas
    
    def mdl_pegar_estudante(nome_estudante, data_matriculas):
        for estudante in data_matriculas:
            if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                matricula_do_estudante = []
                matricula_do_estudante = estudante['matricula']
                return matricula_do_estudante
    
    def mdl_adicionar_matriculas(nome_estudante, pegar_disciplina, data_matriculas):
            encontrou = False
            for estudante in data_matriculas:
                if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                    if disciplinas_disponiveis[pegar_disciplina] in estudante['matricula']:
                        encontrou = 404
                        break
                    else:
                        aux_adicionar = []
                        aux_adicionar.append(disciplinas_disponiveis[pegar_disciplina])
                        estudante['matricula'] += aux_adicionar
                        variavel_auxiliar = data_matriculas
                        encontrou = True
                        return variavel_auxiliar
            if encontrou == False:
                return encontrou
            elif encontrou == 404:
                return encontrou

                    
    def mdl_remover_matriculas(nome_estudante, pegar_disciplina, data_matriculas):
        for estudante in data_matriculas:
            if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                variavel_auxiliar = estudante['matricula']
                pegar_disciplina = variavel_auxiliar[pegar_disciplina]
                if pegar_disciplina not in estudante['matricula']:
                    encontrou = 404
                    break
                else:
                    estudante['matricula'].remove(pegar_disciplina)
                    encontrou = True
                    variavel_auxiliar = data_matriculas
                    return variavel_auxiliar
        if encontrou == False:
            return encontrou
        elif encontrou == 404:
            return encontrou