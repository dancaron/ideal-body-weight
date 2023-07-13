import streamlit as st

# Set title for the app
st.title("Ideal and Adjusted Body Weight Calculator")

# User input fields
gender = st.selectbox("Select your gender", ["Male", "Female"])
height = st.number_input("Enter your height in inches", min_value=1, max_value=120, step=1)
actual_weight = st.number_input("Enter your actual body weight in kg", min_value=1.0, max_value=500.0, step=0.1)

# Function to calculate Ideal Body Weight
def calculate_ibw(gender, height):
    if gender == "Male":
        ibw = 50 + 2.3 * (height - 60)
    else:  # Female
        ibw = 45.5 + 2.3 * (height - 60)

    return ibw

# Function to calculate Adjusted Body Weight
def calculate_adjbw(ibw, actual_weight):
    if actual_weight > ibw:
        adjbw = ibw + 0.4 * (actual_weight - ibw)
    else:
        adjbw = actual_weight

    return adjbw

# Calculate and display Ideal Body Weight
ibw = calculate_ibw(gender, height)
st.text("Your Ideal Body Weight is: {:.2f} kg".format(ibw))

# Calculate and display Adjusted Body Weight
adjbw = calculate_adjbw(ibw, actual_weight)
st.text("Your Adjusted Body Weight is: {:.2f} kg".format(adjbw))
