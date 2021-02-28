from flask                import Flask, Response, request, jsonify
from flask_restful        import Resource, Api
from flask_request_params import bind_request_params

from job import *
from src.pipe.base import (TextProcessing,
                           DateProcessing,
                           OverallProcessing)

# Initialize the restful app
app = Flask(__name__)
api = Api(app)
app.before_request(bind_request_params)

# Create each resource...
api.add_resource(predict_product.PredictProduct, '/v1/categorize')

if __name__ == '__main__':
  app.run(port=5000, debug=True)