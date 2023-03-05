import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import emoji

# Welcome text
st.title('Are you at risk of heart disease? :heart:')
st.write('This application for checking the presence of the risk of heart disease.')
st.write('---')
st.write('Enter your lifestyle information below.')

# Input information about patients
age = st.number_input('How old are you?', 18, 100)
gender = st.radio('What is your gender?', ['Male', 'Female'])
height = st.number_input('How tall are you in cm?', 100, 250)
weight = st.number_input('How much do you weigh in kg?', 40, 300)
ap_hi = st.number_input('Your systolic blood pressure (SBP)?', 60, 240)
ap_lo = st.number_input('Your diastolic blood pressure (DBP)?', 20, 200)
cholesterol = st.selectbox('Your cholesterol level?', [1, 2, 3])
gluc = st.selectbox('Your blood glucose level?', [1, 2, 3])
smoke = st.checkbox('Do you smoke?')
alco = st.checkbox('Do you drink alcohol?')
active = st.checkbox('Do you lead an active lifestyle?')

# Calculation of additional information
# BMI
bmi = round(weight / ((height / 100) ** 2), 1)

def categorize_bmi(bmi):
    if bmi < 16:
        return 1
    if 16 <= bmi < 18.5:
        return 2
    if 18.5 <= bmi <= 24.9:
        return 3
    if 25 <= bmi <= 29.9:
        return 4
    if 30 <= bmi <= 34.9:
        return 5
    if 35 <= bmi <= 39.9:
        return 6
    if bmi >= 40:
        return 7

bmi_category = categorize_bmi(bmi)

# Hypertension
def hypertension(ap_hi, ap_lo):
    if ap_hi < 120 and ap_lo < 80:
        return 1
    if 120 <= ap_hi < 130 and 80 <= ap_lo < 85:
        return 2
    if 130 <= ap_hi < 140 and 85 <= ap_lo < 90:
        return 3
    if 140 <= ap_hi < 160 and 90 <= ap_lo < 100:
        return 4
    if ap_hi >= 160 and ap_lo >= 100:
        return 5
    if ap_hi >= 140 and ap_lo < 90:
        return 6
    return 7

hypertension = hypertension(ap_hi, ap_lo)

# Conversion values to biniary
def gender_to_bin(gender):
    if gender == 'Male':
        return 0
    return 1

def bool_to_bin(bool_value):
    if bool_value == False:
        return 0
    return 1

gender = gender_to_bin(gender)
smoke = bool_to_bin(smoke)
alco = bool_to_bin(alco)
active = bool_to_bin(active)

# Features scaling 
features = pd.read_csv('features_without_scaling.csv') # Processed features without scaling
features_test = [[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi_category, hypertension]]
scaler = StandardScaler()
features = scaler.fit_transform(features)
features_test = scaler.transform(features_test)

# Model
def load():
    with open ('model.pcl', 'rb') as fid:
        return pickle.load(fid)

model = load()
predict = model.predict_proba(features_test)[:, 1][0]

# Results
st.write('---')
if st.button('Calculate Probability'):
    st.subheader('***Your results:***')
    if predict > 0.5:
        st.error('**Your risk of heart diseases: {:.2%}**'.format(predict))
        st.write('Attention\u2757You are at high risk of heart disease! :broken_heart:')
        if hypertension == 4:
            st.write('- You have grade 1 hypertension. Pay attention to your blood pressure. Consult a cardiologist!\U0001f468\U0001f3fb\u200d\u2695\ufe0f')
        if hypertension == 5:
            st.write('- You have grade 2 hypertension. Pay attention to your blood pressure. Consult a cardiologist!\U0001f468\U0001f3fb\u200d\u2695\ufe0f')
        if hypertension == 6:
            st.write('- You have isolated systolic hypertension. Pay attention to your blood pressure. Consult a cardiologist!\U0001f468\U0001f3fb\u200d\u2695\ufe0f')
        if hypertension == 7:
            st.write('- You have an unusual difference between your systolic and diastolic blood pressure readings. This is a reason consult a cardiologist!\U0001f468\U0001f3fb\u200d\u2695\ufe0f')
        if age >= 50:
            st.write('- You are over 50 \U0001f475\U0001f3fb, which means you are at risk for heart disease by age.')
        if cholesterol == 2:
            st.write('- Your cholesterol level is 2. This means that you have a moderate risk of developing vascular atherosclerosis, which affects the presence of heart disease. Consult a therapist!\U0001f469\U0001f3fb\u200d\u2695')
        if cholesterol == 3:
            st.write('- Your cholesterol level is 3. This means that you have a high risk of developing vascular atherosclerosis, which affects the presence of heart disease. Consult a therapist!\U0001f469\U0001f3fb\u200d\u2695')  
    else:
        st.success('**Your risk of heart diseases: {:.2%}**'.format(predict))
        st.write('Great! It looks like you are not at risk of heart disease! :sunglasses:')