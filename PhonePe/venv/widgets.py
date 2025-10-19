import streamlit as st

name=st.text_input('Enter your name:')



if st.button('Click'):
    st.write('Entered Name is ',name,""":sunglasses:""")

address=st.text_area('Enter your address')

st.write(address)

st.date_input('Select any date')

if st.checkbox('terms and conditions'):
    st.write('Thank you :joy:')

radio=st.radio('Colors',['B','G','R','Y'],index=2)

if radio:
    st.write(radio)

msb=st.multiselect('Colors',['B','G','R','Y'])
st.write(msb)

slider=st.slider('age',min_value=10,max_value=60)
st.write(slider)