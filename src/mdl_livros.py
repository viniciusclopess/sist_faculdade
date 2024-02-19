from zz_filtragem import Filtragem
class Livros():
    global data
    data = Filtragem.filtragem_serv_sociais()
    global lista_livros
    lista_livros = []
    global aux_adicionar
    aux_adicionar = []
    global livros_disponiveis
    livros_disponiveis = ["'To Kill a Mockingbird' de Harper Lee", 
    "'Pride and Prejudice' de Jane Austen",
    "'The Diary of Anne Frank' de Anne Frank",
    "'1984' de George Orwell",
    "'Harry Potter and the Sorcerer's Stone' de J.K. Rowling",]

    def __init__(self):
        pass

    def mdl_dados_livros():
        data_livros = data
        nova_chave = 'livros'
        for dicionario in data_livros:
            dicionario[nova_chave] = []
        return data_livros
    
    def mdl_atualizar_dados_livros(data_livros):
        global data
        data = data_livros
        return data
    
    def mdl_livros_disponiveis():
        livros_disponiveis = ["'To Kill a Mockingbird' de Harper Lee", 
        "'Pride and Prejudice' de Jane Austen",
        "'The Diary of Anne Frank' de Anne Frank",
        "'1984' de George Orwell",
        "'Harry Potter and the Sorcerer's Stone' de J.K. Rowling",]
        return livros_disponiveis
    
    def mdl_listar_livros_reservados(nome_estudante, data_livros):
            for estudante in data_livros:
                if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                    lista_livros = estudante['livros']
                    return lista_livros
    
    def mdl_pegar_estudante(nome_estudante, data_livros):
        for estudante in data_livros:
            if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                livros_do_estudante = []
                livros_do_estudante = estudante['livros']
                return livros_do_estudante
            
    def mdl_adicionar_livros(nome_estudante, pegar_livro, data_livros):
            for estudante in data_livros:
                if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                    if livros_disponiveis[pegar_livro] in estudante['livros']:
                        encontrou = 404
                        break
                    else:
                        aux_adicionar = []
                        aux_adicionar.append(livros_disponiveis[pegar_livro])
                        estudante['livros'] += aux_adicionar
                        variavel_auxiliar = data_livros
                        encontrou = True
                        return variavel_auxiliar
            if encontrou == False:
                return encontrou
            elif encontrou == 404:
                return encontrou

    def mdl_remover_livros(nome_estudante, pegar_livro,data_livros):
        for estudante in data_livros:
            if estudante['nome'] == nome_estudante or str(estudante['id']) == nome_estudante:
                variavel_auxiliar = estudante['livros']
                pegar_livro = variavel_auxiliar[pegar_livro]
                if pegar_livro not in estudante['livros']:
                    encontrou = 404
                    break
                else:
                    estudante['livros'].remove(pegar_livro)
                    encontrou = True
                    variavel_auxiliar = data_livros
                    return variavel_auxiliar
        if encontrou == False:
            return encontrou
        elif encontrou == 404:
            return encontrou