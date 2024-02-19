from zz_microsservico import Microsservico
class Filtragem():
    def __init__(self):
        pass

    @classmethod
    def filtragem_serv_sociais(cls):
        db_filtrada = Microsservico.pegar_db()
        estudantes_mantidos = []
        for estudante in db_filtrada:
            if estudante["curso"] != "Serviço Social":    
                pass
            else:
                estudantes_mantidos += [estudante]
        
        # Remove duplicates from estudantes_mantidos
        estudantes_mantidos_no_duplicates = []
        for estudante in estudantes_mantidos:
            if estudante not in estudantes_mantidos_no_duplicates:
                estudantes_mantidos_no_duplicates.append(estudante)
        
        db_filtrada = estudantes_mantidos_no_duplicates
        return db_filtrada