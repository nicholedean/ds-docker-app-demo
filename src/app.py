from flask import Flask
from flask_restful import Api

from src import config
from src.resources.iris import Iris


app = Flask(__name__)
api = Api(app)

api.prefix = '/predict'
api.add_resource(Iris, '/iris')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
