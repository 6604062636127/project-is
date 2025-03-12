import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set the title of your app
st.title('My Streamlit App')

# Show a simple welcome message
st.write('Welcome to the Streamlit app!')

# Example of loading a saved model using joblib
# (Assuming you've saved a model in a file called 'model.pkl')
try:
    model = joblib.load('House.pkl')
    st.write("Model loaded successfully!")
except FileNotFoundError:
    st.write("No model found. Please upload a model.")
    
# Sample input from the user (this could be any input, such as a number or text)
user_input = st.number_input('Enter a number for prediction', min_value=0, max_value=100, value=10)

# If a model is loaded, make predictions
if 'model' in locals():
    prediction = model.predict(np.array([[user_input]]))
    st.write(f'Prediction: {prediction[0]}')

# Add some data visualization or analysis (optional)
# Example: Show a simple DataFrame
data = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
})

st.write('Here is some sample data:')
st.write(data)
