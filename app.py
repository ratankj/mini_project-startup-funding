import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#for more wider page and page title
st.set_page_config(layout='wide',page_title='startup analysis')

#df= pd.read_csv('startup_funding.csv')
df= pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')

# ********************  working on investor dropdown   *******************************************************************

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 incestment of a investor
    last5_df= df[df['investor'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]

    st.subheader('Most Recent Investemnt')
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
    #bigges investemnt
        big_invest_series=df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('largest investment by a investor')

    
    # plotting graph using streamlit
        fig,ax=plt.subplots()
        ax.bar(big_invest_series.index,big_invest_series.values)
        st.pyplot(fig)

    with col2:
    # plotting graph
        vertical_series=df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
    
        st.subheader('Sector invested in')
        fig1,ax1=plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)


    col3,col4=st.columns(2)
    with col3:
    # investemnt at which stage

        investemnt_stage=df[df['investor'].str.contains(investor)].groupby('round')['amount'].sum()

        st.subheader('stage at which invested')
        fig2,ax2=plt.subplots()
        ax2.pie(investemnt_stage,labels=investemnt_stage.index,autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        # city
        
        investemnt_city=df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum()

        st.subheader('city at which invested')
        fig3,ax3=plt.subplots()
        ax3.pie(investemnt_city,labels=investemnt_city.index,autopct="%0.01f%%")
        st.pyplot(fig3)

    # work on year on year graph
    df['year']=df['date'].dt.year
    year_series=df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()

    
    st.subheader('year on year investment')
    fig4,ax4=plt.subplots()
    ax4.plot(year_series.index,year_series.values)
    st.pyplot(fig4)










st.sidebar.title('startup Funding Analysis')

option=st.sidebar.selectbox('select one',['overall analysis','startup','Investor'])

if option == 'overall analysis':

    st.title('overall analysis')

elif option=='startup':

    st.sidebar.selectbox('select startup',sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button('find startup detail')
    st.title('startup analysis')

else:

    selected_investor = st.sidebar.selectbox('select investor',sorted(set(df['investor'].str.split(',').sum())))
    btn2=st.sidebar.button('find startup detail')
    #check button is clicked or not
    if btn2:
        load_investor_details(selected_investor)

    

    