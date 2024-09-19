import logging
import azure.functions as func
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and preprocessor
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("final_model.pkl")

# Define the Azure Function that will handle HTTP requests
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing a request for the Titanic survival prediction.')

    try:
        # Get JSON data from the request
        input_data = req.get_json()

        # Extract features from the input JSON
        age = input_data['age']
        fare = input_data['fare']
        family_size = input_data['family_size']
        sex = input_data['sex']
        embarked = input_data['embarked']
        pclass = input_data['pclass']

        # Convert input data into a pandas DataFrame
        input_features = pd.DataFrame({
            'Age': [age],
            'Fare': [fare],
            'FamilySize': [family_size],
            'Sex': [sex],
            'Embarked': [embarked],
            'Pclass': [pclass]
        })

        # Preprocess the input data
        input_preprocessed = preprocessor.transform(input_features)

        # Make a prediction using the trained model
        prediction = model.predict(input_preprocessed)

        # Return the prediction as JSON
        return func.HttpResponse(
            f'{{"prediction": {int(prediction[0])}}}',
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(
            "Error occurred while processing the request.",
            status_code=400
        )
