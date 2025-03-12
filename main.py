import streamlit as st
import pickle
import pandas as pd

# Load the trained XGBoost model
model = pickle.load(open('model.pkl', 'rb'))

# Set the title of the app
st.title('Car Price Prediction App')

# Create input fields for user data
age = st.selectbox("What is the age of your car?", (1, 2, 3))
hp = st.slider("What is the horsepower of your car?", 60, 200, step=5)
km = st.slider("What is the km of your car?", 0, 100000, step=500)
car_model = st.selectbox("Select model of your car", ('A1', 'A2', 'A3', 'Astra', 'Clio', 'Corsa', 'Espace', 'Insignia'))

# Create a dictionary to hold user inputs
user_input = {
    "age": age,
    "hp": hp,
    "km": km,
    "model": car_model
}

# Convert the dictionary to a DataFrame
input_df = pd.DataFrame.from_dict([user_input])

# Prepare the input for prediction
input_df = pd.get_dummies(input_df).reindex(columns=model.get_booster().feature_names, fill_value=0)

# Make predictions
prediction = model.predict(input_df)

# Display the prediction result
st.success(f"The estimated price of your car is €{int(prediction[0])}.")
