import pandas as pd

from PIL import Image

import streamlit as st
import webbrowser
from streamlit_option_menu import option_menu
import plotly.express as px

import folium





df_aggregated_transaction=pd.read_csv("aggregated_transaction.csv")
df_aggregated_user=pd.read_csv("aggregated_user.csv")
df_map_transaction=pd.read_csv("map_transaction.csv")
df_map_user=pd.read_csv("map_user.csv")
df_top_transaction=pd.read_csv("top_transaction.csv")
df_top_user=pd.read_csv("top_user.csv")

#background
im = Image.open("phonepe-logo-icon.PNG")
st.set_page_config(
    page_title="Phonepe Pulse Insights",
    page_icon=im,
    layout="wide",
)
st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url("Background.jpg");
    background-attachment: fixed;
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

#display

st.title(":blue[PhonePe Pulse]")


geo=Image.open("geolocation.png")
Dashboard=Image.open("dashboard.png")

selected=option_menu(
    menu_title = None,
    options=["HOME", "GEO-INSIGHTS","DASHBORD" ],
    icons =["house","map","bar-chart"],
    orientation = "horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0c7ded"},
        "icon": {"color": "black", "font-size": "17px"},
        "nav-link": {"font-size": "17px", "text-align": "center", "margin":"2px", "--hover-color": "#1e0ead"},
        "nav-link-selected": {"background-color": "#1e0ead"},
    }
)


    
    
if selected == "HOME":
    st.subheader("Introduction")
    st.write("""The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution 
            being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the 
            central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. 
            When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving 
            back to the digital payments ecosystem.""")
    st.subheader("GUIDE")
    st.write(""" This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.""")
    with st.expander("Aggregated"):
        st.write("Aggregated values of various payment categories as shown under Categories section")
        #st.write(df_aggregated_transaction.groupby(['Transaction_type'])['Transaction_count'].sum())
    with st.expander("Map"):
        st.write("Total values at the State and District levels")
    with st.expander("Top"):
        st.write("TTotals of top States / Districts / Pin Codes")
    st.subheader("Github")
    st.write("A home for the data that powers the PhonePe Pulse website.")
    if st.button('Open'):
        webbrowser.open_new_tab("https://github.com/PhonePe/pulse#readme")
    st.write("To unleash the power of information and to give back to the ecosystem and the developer community, we decided to open the anonymised aggregate data sets that demystify the what, why and how of digital payments in India. Licensed under the CDLA-Permissive-2.0 open data license, the PhonePe Pulse Dataset API is a first-of-its-kind open data initiative in the payments space.")
    
if selected == "GEO-INSIGHTS":
    
    with st.sidebar:
        Menu=st.selectbox("",('Transactions',"User"))
        year= st.selectbox("Select Year",(2018, 2019, 2020, 2021, 2022))
        Quarter=st.selectbox('select a Quarter',(1,2,3,4))
    if Menu=="Transactions":
        metric = st.selectbox('Select an indicator', options=['count', 'amount'])
        
        df=df_map_transaction[(df_map_transaction['Year']==year) & (df_map_transaction['Quarter']==Quarter)]
        st.title("Interactive Dashboard")
        df_map = df[['State', 'count']].groupby(['State']).sum().reset_index()
        # Create a Plotly Choropleth map using the filtered dataframe
        fig = px.choropleth(df, 
                    locations='State', 
                    color='amount',
                    geojson='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data',
                    featureidkey='properties.name',
                    animation_frame='Year',
                    color_continuous_scale='YlGnBu',
                    title='Amount by State')
        fig.update_geos(fitbounds="locations", visible=False)
        
        # Display the Plotly map in Streamlit
        st.plotly_chart(fig)
        
        
if selected == "DASHBORD":
    
    
    selected = option_menu(menu_title=None, 
                           options=["Aggregated Data Insights",
                                    "Map Data Insights",
                                    "Top Data Insights"
                                      ], 
                           orientation = "horizontal",
                           styles={
                               "container": {"padding": "0!important", "background-color": "#09dbc3"},
                               "icon": {"color": "black", "font-size": "15px"},
                               "nav-link": {"font-size": "15px", "text-align": "center", "margin":"6px", "--hover-color": "white"},
                               "nav-link-selected": {"background-color": "#1e0ead"},
                           })
    
    
    with st.sidebar:
        st.header=None
        menu=st.selectbox("",('Transactions',"User"))
        year= st.selectbox("Select Year",(2018, 2019, 2020, 2021, 2022))
        Quarter=st.selectbox('select a Quarter',(1,2,3,4))
        
        #with st.sidebar:
    
            
    if selected=="Aggregated Data Insights":
        if menu=='Transactions':
            menu2=  st.sidebar.selectbox('Transaction Count or Transaction amount',("Transaction_count","Transaction_amount"))
            df=df_aggregated_transaction[(df_aggregated_transaction['Year']==year) & (df_aggregated_transaction['Quarter']==Quarter) ]
            
            #Bar Plots
            fig = px.bar(df, x='State', y=menu2, color='State', 
                 title='Transaction Count/amount by State')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.bar(df, x='Transaction_type', y=menu2, color='State',
                          title='Transaction Count/amount by Transaction_type')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.scatter(df, x='Transaction_amount', y='Transaction_count', color='State',
                          title='Transaction Amount by Transaction_count')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.area(df, x='Transaction_type', y=menu2, color='State',
                          title='Transaction Count/amount Transaction_type')
            
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.pie(df, values=menu2, names='Transaction_type', title='Percent of Transaction_type')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
        if menu=='User':
            
            df=df_aggregated_user[(df_aggregated_user['Year']==year) & (df_aggregated_user['Quarter']==Quarter) ]
            menu2=  st.sidebar.selectbox('Transaction Count or Transaction Percentage',("Count","Percentage"))
            
            fig = px.pie(df, values=menu2, names='brands', title='Percent of brands')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            #Bar Plots
            fig = px.bar(df, x='State', y=menu2, color='State', 
                 title='Transaction Count/amount by State')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.bar(df, x='brands', y=menu2, color='State',
                          title='Transaction Count/amount by Transaction_type')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.scatter(df, x='Count', y='Percentage', color='State',
                          title='Transaction Amount by Transaction_count')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
    if selected=="Map Data Insights":
        if menu=='Transactions':
            
            menu2=  st.sidebar.selectbox('Transaction Count or Transaction amount',("count","amount"))
            df=df_map_transaction[(df_map_transaction['Year']==year) & (df_map_transaction['Quarter']==Quarter) ]
            
            #Bar Plots
            fig = px.bar(df, x='State', y=menu2, color='State', 
                 title='Transaction Count/amount by State')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.bar(df, x='District', y=menu2, color='State',
                          title='Transaction Count/amount by District')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.scatter(df, x='amount', y='count', color='State',
                          title='Transaction Amount by Transaction_count')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.area(df, x='District', y=menu2, color='State',
                          title='Transaction Count/amount by District')
            
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
           
        if menu=='User':
            
            df=df_map_user[(df_map_user['Year']==year) & (df_map_user['Quarter']==Quarter) ]
           
            
            
            fig = px.bar(df, x='District', y='RegisteredUser', color='State', 
                 title='Registered Users by State')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            
            fig = px.bar(df, x='State', y='RegisteredUser', color='State', 
                 title='Registered Users by State')
            st.plotly_chart(fig, use_container_width=False, theme="streamlit")
    if selected=="Top Data Insights":
         if menu=='Transactions':
             
             menu2=  st.sidebar.selectbox('Transaction Count or Transaction amount',("Transaction_count","Transaction_amount"))

             df=df_top_transaction[(df_top_transaction['Year']==year) & (df_top_transaction['Quarter']==Quarter) ]
             
             #Bar Plots
             fig = px.bar(df, x='State', y=menu2, color='State', 
                  title='Transaction Count/amount by State')
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
             
             fig = px.bar(df, x='District', y=menu2, color='State',
                           title='Transaction Count/amount by District')
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
             
             fig = px.scatter(df, x='Transaction_amount', y='Transaction_count', color='State',
                           title='Transaction Amount by Transaction_count')
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
             
             fig = px.area(df, x='District', y=menu2, color='State',
                           title='Transaction Count/amount by District')
             
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
             
            
         if menu=='User':
             
             df=df_top_user[(df_top_user['Year']==year) & (df_top_user['Quarter']==Quarter) ]
            
             
             
             fig = px.bar(df, x='District', y='RegisteredUser', color='State', 
                  title='Registered Users by State')
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
             
             fig = px.bar(df, x='State', y='RegisteredUser', color='State', 
                  title='Registered Users by State')
             st.plotly_chart(fig, use_container_width=False, theme="streamlit")
            

            
            
            
    

        

    


