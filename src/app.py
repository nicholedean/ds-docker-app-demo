from flask import Flask
from flask_restful import Api

from src.config import default
from src.resources.iris import Iris

# Create the Flask app
app = Flask(__name__)

# Load configuration vals default
app.config.from_object(default)

# Load configuration vals based on env
app.config.from_envvar('APP_ENV_CONFIG', silent=True)

# Create restful api flask app, add all resources require
api = Api(app)
api.prefix = '/predict'
api.add_resource(Iris, '/iris')


if __name__ == '__main__':
    app.run('0.0.0.0', app.config['PORT'], debug=app.config['DEBUG'])
