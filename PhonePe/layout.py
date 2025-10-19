import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

r=st.sidebar.radio('Navigation',['Home','Operation'])


if r=='Operation':

    data={

        'Number':[x for x in range(1,11)],
        'Square of the number':[x**2 for x in range(1,11)],
        'Twice of the number':[x*2 for x in range(1,11)]

    }

    df=pd.DataFrame(data) 

    col=st.sidebar.selectbox('select any Number',df.columns)
    # st.write(col)

    fig,ax=plt.subplots()
    ax.plot(df['Number'],df[col])

    ax.set_title(f'Number vs {col}')
    ax.set_xlabel('Number')
    ax.set_ylabel(col)
    st.pyplot(fig)

if r=='Home':
    st.balloons()