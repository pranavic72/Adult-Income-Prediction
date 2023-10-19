from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import joblib
from PIL import Image

st.title('WELCOME')
st.header('ADULT CENSUS INCOME PREDICTION')
st.write('The main objective behind our project is to predict if a said person, given his attributes, earns more than $50k per annum or not.')
image = Image.open('Adult_Census_img.png')
st.image(image)
st.write('NOTE: The users are requested to provide the Input to the form below and Click the Submit button to get the result')
#Getting Inputs from Users
with st.form(key = 'my_form'):
    #Age Input
    age = st.number_input('Enter The Age in range between 20 t0 65:',min_value=20,max_value=65)
    final_age = (age - 38.581)/13.640

    #Workclass Input
    workclass = st.selectbox('Select the Workclass',(' State-gov',
    ' Self-emp-not-inc',
    ' Private',
    ' Federal-gov',
    ' Local-gov',
    ' private',
    ' Self-emp-inc',
    ' Without-pay',
    ' Never-worked'))
    d_workclass = {' State-gov': 6, ' Self-emp-not-inc': 5, ' Private': 3, ' Federal-gov': 0, ' Local-gov': 1, ' private': 8, ' Self-emp-inc': 4, ' Without-pay': 7, ' Never-worked': 2}
    final_workclass = (d_workclass[workclass] - 3.3763705045913825)/1.5820377206943912

    #EDUCATION INPUT
    education = st.selectbox('Select the Eduction Deatils:',(' undergrad', ' High-school', ' school', ' Postgrad', ' Doctorate'))
    d_education = {' undergrad': 4, ' High-school': 1, ' school': 3, ' Postgrad': 2, ' Doctorate': 0}
    final_education = (d_education[education]-2.709929056232917)/1.3617186344156296

    #MARITAL INPUT
    marital = st.selectbox('Marital Status',(' un-married', ' Married', ' others'))
    d_marital = {' un-married': 2, ' Married': 0, ' others': 1}
    final_marital = (d_marital[marital] - 0.8546113448604158)/0.8834356464150362

    #OCCUPATION INPUT
    occupation = st.selectbox('Occupation:',(' Adm-clerical', ' Executive-managerial', ' Handlers-cleaners',
        ' Prof-specialty', ' Other-services', ' Sales', ' Craft-repair',
        ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
        ' Tech-support', ' Protective-servives', ' Armed-Forces',
        ' Priv-house-serv'))
    d_occupation = {' Adm-clerical': 0, ' Executive-managerial': 3, ' Handlers-cleaners': 5, ' Prof-specialty': 9, ' Other-services': 7, ' Sales': 11, ' Craft-repair': 2, ' Transport-moving': 13, ' Farming-fishing': 4, ' Machine-op-inspct': 6, ' Tech-support': 12, ' Protective-services': 10, ' Armed-Forces': 1, ' Priv-house-serv': 8}
    final_occupation = (d_occupation[occupation] - 6.138754952243482)/3.972707508561352

    #RELATION INPUT
    relation = st.selectbox('Relationship:',(' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried',
        ' Other-relative'))
    d_relation = {' Not-in-family': 1, ' Husband': 0, ' Wife': 5, ' Own-child': 3, ' Unmarried': 4, ' Other-relative': 2}
    final_relation = (d_relation[relation] - 1.4463622124627622)/1.6067709504166081

    #SEX INPUT
    sex = st.radio('SEX:',('Male','Female'))
    d_sex = {'Male':0, 'Female':1}
    final_sex = d_sex[sex]

    #HRS INPUT
    hrs = st.number_input('Hours Per Week',max_value = 99,min_value=1)
    final_hrs = (hrs - 39.37793679555296)/12.144005798600519


    #country input
    country = st.selectbox('Choose The Country',(' United-States', ' Cuba', ' Jamaica', ' India', ' Mexico',
        ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada',
        ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland',
        ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos',
        ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
        ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
        ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
        ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
        ' Ireland', ' Hungary', ' Holand-Netherlands'))
    d_country = {' United-States': 38, ' Cuba': 4, ' Jamaica': 22, ' India': 18, ' Mexico': 25, ' South': 34, ' Puerto-Rico': 32, ' Honduras': 15, ' England': 8, ' Canada': 1, ' Germany': 10, ' Iran': 19, ' Philippines': 29, ' Italy': 21, ' Poland': 30, ' Columbia': 3, ' Cambodia': 0, ' Thailand': 36, ' Ecuador': 6, ' Laos': 24, ' Taiwan': 35, ' Haiti': 13, ' Portugal': 31, ' Dominican-Republic': 5, ' El-Salvador': 7, ' France': 9, ' Guatemala': 12, ' China': 2, ' Japan': 23, ' Yugoslavia': 40, ' Peru': 28, ' Outlying-US(Guam-USVI-etc)': 27, ' Scotland': 33, ' Trinadad&Tobago': 37, ' Greece': 11, ' Nicaragua': 26, ' Vietnam': 39, ' Hong': 16, ' Ireland': 20, ' Hungary': 17, ' Holand-Netherlands': 14} 
    final_country = (d_country[country] - 36.41715549276742)/6.056046527027436

        
    #USING SUBMIT BUTTON FOR FORM and Displaying output
    submit_button = st.form_submit_button(label = 'Submit')
    if submit_button:
        final_list = [final_age,final_workclass,final_education,final_marital,final_occupation,final_relation,final_sex,final_hrs,final_country]
        load_rfc = joblib.load('./Model/Adult_census_prediction.sav')
        ans = load_rfc.predict([final_list])
        if(ans[0] == 0):
            st.write('This Person Earns less than 50K Dollars Per year')
        else:
            st.write('This Person Earns more than 50k Dollars per year')

