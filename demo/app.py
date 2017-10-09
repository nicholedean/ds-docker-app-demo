import numpy as np

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import provider

app = Flask(__name__)
api = Api(app)


class Prediction(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('slength', type=float,
                            help='slength cannot be converted.')
        parser.add_argument('swidth', type=float,
                            help='swidth cannot be converted.')
        parser.add_argument('plength', type=float,
                            help='plength cannot be converted.')
        parser.add_argument('pwidth', type=float,
                            help='pwidth cannot be converted.')
        args = parser.parse_args()

        prediction = provider.predict(np.array([
            args['slength'],
            args['swidth'],
            args['plength'],
            args['pwidth']
        ]))

        print('The prediction is %s' % prediction)

        return {
            'slength': args['slength'],
            'swidth': args['swidth'],
            'plength': args['plength'],
            'pwidth': args['pwidth'],
            'species': prediction[0]
        }


api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
