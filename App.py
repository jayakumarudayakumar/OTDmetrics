import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
import joblib

# Function to categorize discount
def categorize_discount(discount):
    if 0 <= discount <= 5:
        return 'Low'
    elif 5 < discount <= 20:
        return 'Medium'
    elif 20 < discount <= 100:
        return 'High'
    else:
        return 'Undefined'

# Function to categorize weight
def categorize_weight(weight):
    if 0 <= weight <= 1899:
        return 'Low'
    elif 1900 <= weight <= 4199:
        return 'Medium'
    elif 4200 <= weight <= 9000:
        return 'High'
    else:
        return 'Undefined'

# Load the trained model
model = joblib.load(r'C:\Users\anoop\OneDrive\MS\1st Quarter\Data Mining ALY6040\Data mining Project\trained_model.joblib')

# Streamlit UI components
st.title('Delivery Prediction')

# User Inputs
warehouse_block = st.selectbox('Warehouse Block', ['A', 'B', 'C', 'D', 'F'])
mode_of_shipment = st.selectbox('Mode of Shipment', ['Flight', 'Ship', 'Road'])
customer_care_calls = st.number_input('Customer Care Calls', min_value=1, max_value=7, value=3)
customer_rating = st.number_input('Customer Rating', min_value=1, max_value=5, value=3)
cost_of_the_product = st.number_input('Cost of the Product (USD)', min_value=1, value=100)
prior_purchases = st.number_input('Prior Purchases', min_value=1, value=3)
product_importance = st.selectbox('Product Importance', ['low', 'medium', 'high'])
gender = st.selectbox('Gender', ['F', 'M'])
discount_offered = st.number_input('Discount Offered', min_value=0, max_value=100, value=0)
weight_in_gms = st.number_input('Weight in grams', min_value=0, max_value=20000, value=0)


if st.button('Predict'):
    # Preprocess the input
    Discount_Range = categorize_discount(discount_offered)
    Weight_Range = categorize_weight(weight_in_gms)
    
    # Create a DataFrame with the input features
    input_df = pd.DataFrame({
        'Warehouse_block': [warehouse_block],
        'Mode_of_Shipment': [mode_of_shipment],
        'Customer_care_calls': [customer_care_calls],
        'Customer_rating': [customer_rating],
        'Cost_of_the_Product': [cost_of_the_product],
        'Prior_purchases': [prior_purchases],
        'Product_importance': [product_importance],
        'Gender': [gender],
        'Discount_offered': [discount_offered],
        'Weight_in_gms': [weight_in_gms],
        'Discount_Range': [Discount_Range],
        'Weight_Range': [Weight_Range]
    })
    
    # Making predictions
    prediction = model.predict(input_df)
    
    # Display the prediction
    if prediction[0] == 1:
        st.success('The delivery is predicted to be on time!')
    else:
        st.error('The delivery is predicted not to be on time!')

