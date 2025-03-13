import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Housing Prices Prediction")
st.write("Enter the details below:")

# Input fields
area = st.number_input("Area (in square meters)", min_value=0.0, value=100.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=1)

# Button to make prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        # Add other features as necessary
    })

    # Make prediction
    predicted_price = model.predict(input_data)
    st.write(f"Predicted Price: {predicted_price[0]:,.2f} Baht")
