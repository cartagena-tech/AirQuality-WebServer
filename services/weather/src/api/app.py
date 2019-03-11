# services/weather/src/api/app.py

from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc

home_blueprint = Blueprint('home', __name__, template_folder='./templates')

@home_blueprint.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'success',
        'api': 'v1!'
    })
