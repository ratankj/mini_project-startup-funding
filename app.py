import streamlit as st
import pandas as pd

df= pd.read_csv('startup_funding.csv')

df['Investors Name']= df['Investors Name'].fillna('Undisclosed')

st.sidebar.title('startup Funding Analysis')

option=st.sidebar.selectbox('select one',['overall analysis','startup','Investor'])

if option == 'overall analysis':

    st.title('overall analysis')

elif option=='startup':

    st.sidebar.selectbox('select startup',sorted(df['Startup Name'].unique().tolist()))
    btn1=st.sidebar.button('find startup detail')
    st.title('startup analysis')

else:

    st.sidebar.selectbox('select investor',sorted(df['Investors Name'].unique().tolist()))
    btn2=st.sidebar.button('find startup detail')
    st.title('investor analysis')