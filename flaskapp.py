from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and preprocessor
preprocessor = joblib.load("preprocessor.pkl")  # Load the preprocessing pipeline
model = joblib.load("final_model.pkl")  # Load the trained model

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    input_data = request.json
    
    # Extract features from the input JSON
    age = input_data['age']
    fare = input_data['fare']
    family_size = input_data['family_size']
    sex = input_data['sex']
    embarked = input_data['embarked']
    pclass = input_data['pclass']
    
    # Convert the input data to a pandas DataFrame
    input_features = pd.DataFrame({
        'Age': [age],
        'Fare': [fare],
        'FamilySize': [family_size],
        'Sex': [sex],
        'Embarked': [embarked],
        'Pclass': [pclass]
    })
    
    # Preprocess the input using the pre-trained preprocessor
    input_preprocessed = preprocessor.transform(input_features)
    
    # Predict the class using the pre-trained model
    prediction = model.predict(input_preprocessed)
    
    # Return the prediction result as JSON
    return jsonify({'prediction': int(prediction[0])})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
