import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model and preprocessor
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("final_model.pkl")

# Streamlit UI for user input
st.title("Titanic Survival Prediction")

# Create two columns for the input fields
col1, col2 = st.columns(2)

# Input fields for the features in two columns
with col1:
    age = st.number_input("Age", min_value=0, max_value=100, value=25)
    fare = st.number_input("Fare", min_value=0.0, max_value=1000.0, value=50.0)
    family_size = st.number_input("Family Size", min_value=1, max_value=10, value=1)

with col2:
    sex = st.selectbox("Sex", options=["male", "female"])  # Categorical feature
    embarked = st.selectbox("Embarked", options=["C", "Q", "S"])  # Categorical feature
    pclass = st.selectbox("Pclass", options=[1, 2, 3])  # Categorical feature

# Button for making predictions
if st.button("Predict Survival"):
    # Convert input data into a pandas DataFrame
    input_features = pd.DataFrame({
        'Age': [age],
        'Fare': [fare],
        'FamilySize': [family_size],
        'Sex': [sex],
        'Embarked': [embarked],
        'Pclass': [pclass]
    })

    # Debugging: Check input values
    st.write("Input Features DataFrame:")
    st.write(input_features)
    
    # Preprocess the input using the pre-trained preprocessor
    try:
        input_preprocessed = preprocessor.transform(input_features)  # Preprocess the input
        
        # Print the preprocessed shape and compare it with what the model expects
        st.write(f"Preprocessed Input Shape: {input_preprocessed.shape}")
        
        # Predict the class using the pre-trained model
        prediction = model.predict(input_preprocessed)[0]
        
        # Display the result
        if prediction == 1:
            st.success("Prediction: Survived")
        else:
            st.error("Prediction: Not Survived")
    
    except Exception as e:
        st.error(f"Error occurred during preprocessing: {e}")

# Compare the expected number of features from the preprocessor
try:
    # Create a sample input to check the expected number of features after transformation
    sample_input = pd.DataFrame({
        'Age': [25],
        'Fare': [50.0],
        'FamilySize': [1],
        'Sex': ['male'],
        'Embarked': ['C'],
        'Pclass': [1]
    })
    transformed_sample = preprocessor.transform(sample_input)
    expected_shape = transformed_sample.shape[1]
    st.write(f"Expected number of features after preprocessing: {expected_shape}")
except Exception as e:
    st.error(f"Error occurred during shape check: {e}")
