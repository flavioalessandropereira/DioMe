from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'C++', 'VB', 'Rubi','Delphi', 'Flask']

class Habilidades(Resource):
    def get (self):
        return lista_habilidades
