from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'C++', 'VB', 'Rubi','Delphi', 'Flask']

#A lista de Habilidades estará disposta no arquivo app_restful.py para ser utilizado
class Habilidades(Resource):
    def get (self):
        return lista_habilidades
