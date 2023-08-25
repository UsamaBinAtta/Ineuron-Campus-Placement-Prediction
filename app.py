import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_path = r"C:\Users\usama\PycharmProjects\placement-prediction\placed_model.pkl"

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Create the Streamlit web app
st.title("Campus Placement System")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
ssc_p = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0)
hsc_p = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0)
degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0)
degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.selectbox("Work Experience", ["No", "Yes"])
etest_p = st.number_input("ETest Percentage", min_value=0.0, max_value=100.0)
specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0)

# Convert input values to coded values
if gender == 'Male':
    gender_code = 0
else:
    gender_code = 1

if degree_t == 'Sci&Tech':
    degree_t_code = 2
elif degree_t == 'Comm&Mgmt':
    degree_t_code = 0
else:
    degree_t_code = 1

if workex == 'Yes':
    workex_code = 1
else:
    workex_code = 0
if hsc_s == 'Commerce':
    hsc_s1 = 1
elif hsc_s == 'Science':
    hsc_s1 = 2
else:
    hsc_s1 = 0

if specialisation == 'Mkt&HR':
    specialisation1 = 1
else:
    specialisation1 = 0
# Prepare input data
input_data = pd.DataFrame({
    'gender': [gender_code],
    'ssc_p': [ssc_p],
    'hsc_p': [hsc_p],
    'degree_p': [degree_p],
    'degree_t': [degree_t_code],
    'workex': [workex_code],
    'etest_p': [etest_p],
    'specialisation': [specialisation_code],
    'mba_p': [mba_p]
})

# Create a "Check Result" button
if st.button("Check Result"):
    prediction = model.predict(input_data)[0]
    if prediction == 0:
        st.write("The person isn't placed.")
    else:
        st.write("The person is placed.")
