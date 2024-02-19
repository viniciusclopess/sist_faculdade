import requests
import os
class Microsservico():
    def __init__(self):
        pass

    @classmethod
    def pegar_db(cls):
        os.system("cls")
        response = requests.get("https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno")
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("Erro na requisição")