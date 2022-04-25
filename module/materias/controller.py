from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.materias.model import Materias
from module.materias.dao import MateriaDao

dao = MateriaDao(connectDataBase=ConnectDataBase())

app_materias = Blueprint("app_materias", __name__)
app_name = "materias"


@app_materias.route(f'/{app_name}/', methods=["GET"])
def getAll_materias():
    materias = dao.getAll_Materias()

    return make_response(jsonify(materias), 200)

@app_materias.route(f'/{app_name}/adicionar/', methods=['POST'])
def add_materia():
    data = request.form.to_dict(flat=True)
    materia = None
    try:
        materia = Materias(**data)
        materia = dao.save_Materia(materia)
    except Exception as e:
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
            }, 400)
    return make_response({'id': materia.id}, 200)
