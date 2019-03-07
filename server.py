#!/home/phantom/.virtualenvs/flask/bin/python
from flask import Flask, render_template, url_for, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

data = []

@app.route('/')
def home():
    url_for('static', filename='style.css')
    return render_template('index.html')

@app.route('/put')
def put_data():
    ip = request.args.get('ip')
    irms = request.args.get('irms')
    p = request.args.get('p')
    if len(data) > 9:
        del data[0]
    data.append({'ip':ip, 'irms':irms, 'p':p})
    return 'Data saved', 200

@app.route('/get')
def get_data():
    return jsonify(data=data)

app.run(host='0.0.0.0', debug=True)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

api.add_resource(User, "/user/<string:name>")

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
