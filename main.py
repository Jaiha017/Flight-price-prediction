import streamlit as st
import pandas as pd
import pickle
import joblib

# ------------------------------
# Load trained model
# ------------------------------
model = joblib.load(r"C:\Users\user\Desktop\Flight\model\flight_price_model.pkl")

st.title("✈️ Flight Price Prediction App")
st.write("Enter flight details to get the predicted ticket price.")

# ------------------------------
# User Inputs
# ------------------------------
airline = st.selectbox("Airline", [
    "Air India","Indigo","SpiceJet","Vistara","GoAir","AirAsia"
])

source_city = st.selectbox("Source City", [
    "Delhi","Mumbai","Bangalore","Chennai","Kolkata","Hyderabad"
])

destination_city = st.selectbox("Destination City", [
    "Delhi","Mumbai","Bangalore","Chennai","Kolkata","Hyderabad"
])

departure_time = st.selectbox("Departure Time", [
    "Morning","Evening","Night","Afternoon","Early Morning","Late Night"
])

arrival_time = st.selectbox("Arrival Time", [
    "Morning","Evening","Night","Afternoon","Early Morning","Late Night"
])

stops = st.selectbox("Stops", ["zero","one","two_or_more"])

flight_class = st.selectbox("Class", ["Economy", "Business"])

duration = st.number_input("Duration (hours)", min_value=0.5, step=0.5)
days_left = st.number_input("Days Left for Departure", min_value=0, step=1)

# ------------------------------
# Predict Button
# ------------------------------
if st.button("Predict Price"):
    # Create a DataFrame with user input
    new_data = pd.DataFrame({
        "airline": [airline],
        "flight": ["NA"],   # if model had 'flight' column, placeholder
        "source_city": [source_city],
        "departure_time": [departure_time],
        "stops": [stops],
        "arrival_time": [arrival_time],
        "destination_city": [destination_city],
        "class": [flight_class],
        "duration": [duration],
        "days_left": [days_left]
    })

    # Predict price
    predicted_price = model.predict(new_data)
    st.success(f"💰 Predicted Ticket Price: ₹ {predicted_price[0]:,.2f}")
