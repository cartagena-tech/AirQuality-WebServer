# services/weather/src/api/stations.py
"""Station function views."""

# flask
from flask import Blueprint, jsonify, request, render_template
# sqlalchemy
from sqlalchemy import exc

# Models
from src.api.models import CurrentCondition
# Instance db
from src import db

# Blueprint
home_blueprint = Blueprint('home', __name__, template_folder='./templates')
stations_blueprint = Blueprint('stations',__name__,template_folder='./templates')

@home_blueprint.route('/', methods=['GET'])
def home():
    return jsonify({
        'API': 'Weather',
        'version': 'v1!'
    })


@stations_blueprint.route('/app', methods=['GET', 'POST'])
def index():
    """ Index app.
    """
    return render_template('index.html')


@stations_blueprint.route('/station/create',methods=['GET'])
def create_station():
    """ Create station.
    create station used the method get http,this endpoint get data from device and save in database
    """
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')
    pm2 = request.args.get('pm2')

    try:
        station=CurrentCondition(
                temperature=temperature,
                humidity=humidity,
                pm=pm2,
                station=1
        )
        db.session.add(station)
        db.session.commit()
        return jsonify({"station": station.to_json()}),201
    except Exception as e:
        return(str(e))

""" @stations_blueprint.route('/station/create',  methods=['POST'])
def create_station():
    post_data = request.get_json()
    return jsonify({'data': post_data}) """


@stations_blueprint.route('/stations', methods=['GET'])
def get_data_station():
    """Get all  data station"""
    response_object = {
        'status': 'success',
        'weather': {
            'station': [station.to_json() for station in CurrentCondition.query.all()]
        }
    }
    return jsonify(response_object), 200
