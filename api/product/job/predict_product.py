"""
"""
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
from flask_request_params import bind_request_params

import json
import joblib
import pandas as pd
from datetime import datetime
from src.pipe.base import (TextProcessing,
                           DateProcessing,
                           OverallProcessing)

# Loading models
MODEL = joblib.load("models/model.joblib")
PIPELINE = joblib.load("models/pipeline.joblib")
LABEL_ENCODER = joblib.load("models/label_encoder.joblib")

class PredictProduct(Resource):
    """
    """
    
    def post(self):
        """
        """
        # Build response model
        response = Response(mimetype='application/json')
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.status_code = 400
        # Get request body
        payload_data = request.get_json()
        try:
            # Building processing DataFrame
            df = pd.DataFrame(payload_data["products"])
            df['creation_date'] = df['creation_date'].apply(
                lambda t: datetime.strptime(t,'%d/%m/%Y'))
            # Make product prediction
            X_ = PIPELINE.transform(df)
            y_hat = MODEL.predict(X_)
            pred_labels = (
                LABEL_ENCODER
                .inverse_transform(y_hat)
                .tolist()
            )
            # Build output
            response.response = json.dumps(
                {"categories": pred_labels})
            response.status_code = 200
        except Exception as e:
            response.response = json.dumps(
                {"error": str(e)})
        return response

        

    