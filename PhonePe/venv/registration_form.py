import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Registration Form')

# creating the form
form=st.form(key='registraition_form')
#Input fields
name=form.text_input('Enter your name')
email=form.text_input('Enter your Email')
password=form.text_input('Enter your password',type='password')
dob=form.date_input('Select Date')
gender=form.radio('Gender',['Male','Female'])
country=form.selectbox('Country',['India','US','UK'])

submit_button=form.form_submit_button(label='Registration')

if submit_button:
    data={
        'Name':name,
        'Email':email,
        'Password':password,
        'Date of Birth':dob,
        'Gender':gender,
        'Country':country
    }

    df=pd.DataFrame([data])

    #display df
    st.table(df)