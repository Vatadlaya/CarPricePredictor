import streamlit as st
import numpy as np
import pickle

# Load trained Random Forest regression model
# Open the file in read-binary ('rb') mode and load the model
model =  pickle.load(open('rf_model.pkl', 'rb'))

# Streamlit User Interface (UI):
st.set_page_config(page_title="Used Car Price Predictor", layout="centered")
# This line of code sets the basic configuration for a Streamlit web application
# st.set_page_config(page_title="Used Car Price Predictor", layout="centered")
# Defines the browser tab settings, including the title, icon, and layout, and must be the first Streamlit command in the script.
# layout="centered":
# layout="centered": Constrains the app's content to a narrow, centered column, which is the default behavior if not specified.
st.title("🚗 Used Car Price Prediction") # Title for a Streamlit app, 
# This is a popular Python framework used to build interactive web applications for data science and machine learning
st.markdown("Enter the details of the car below to predict its price.")
# This is used for instructing users to enter car details for a price prediction app in Streamlit

# Input fields:
kms = st.number_input("Kilometers Driven", min_value=0, max_value=300000, step=1000)
age = st.number_input("Age of the Car (in years)", min_value=0, max_value=25, step=1)
oprice = st.number_input("Original Price (Rs.)", min_value=500000, max_value=5000000, step=10000)
# This Streamlit code creates an integer input widget labeled "Kilometers Driven". 
# Users can select values between 0 and 300,000, increasing or decreasing by 1,000 units, which is ideal for vehicle mileage 

# Conditions
# --- ADD THIS LINE BEFORE YOUR CODE ---
fuel_type = "petrol"  # Example assignment
# Fixed Version
fuel_type = fuel_type.capitalize() 

if fuel_type == 'Petrol':
    fuel = [0.0, 0.0, 1.0]
elif fuel_type == 'Diesel':
    fuel = [0.0, 1.0, 0.0]
elif fuel_type == 'Cng':
    fuel = [1.0, 0.0, 0.0]
else:
    fuel = [0.0, 0.0, 0.0]

# Add this line before your code:
transmission = "Automatic"
if transmission == 'Automatic':
    transmission_vals = [1.0, 0.0]
else:
    transmission_vals = [0.0, 1.0]

# Prediction
if st.button("🔮 Predict Price"):
    data = np.array([[oprice, kms, age, 
                  fuel[0], fuel[1], fuel[2], 
                  transmission_vals[0], transmission_vals[1]]])

    result = np.round(model.predict(data))
    st.success(f"Predicted Car Price: ({result[0]:,.0f}")