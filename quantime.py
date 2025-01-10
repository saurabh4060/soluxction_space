import streamlit as st
import plotly.express as px
import pandas as pd
import os #to navigate some file if needed
import warnings
warnings.filterwarnings('ignore')#to ignore warnings

st.set_page_config(page_title="Quantime",page_icon=":bar_chart",layout='wide')
st.title(" :bar_chart:  Quantime")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)
file=st.file_uploader(":file_folder: upload file")
user=0
username=st.text_input("Enter Your Name")
password=st.text_input("Enter pass")
if username=="Saurabh" and password=="1234":
    accsess=1
    st.write(f"hello {username} Welcome" )
    
    if file is not None:
        st.write(file)
        df=pd.read_csv("quantime_clean.csv")
        st.subheader("From our dataset it will Show the of Five Number Summary Columns ")
        st.dataframe(df.describe())
        st.write("Select From below")
        st.write("1.Bar Chart")
        st.write("2.Pie Chart")
        user=st.selectbox("What type of visual you want to see",[0,1,2,3],index=0)
        st.write(user)

    if user==1.0:
        st.subheader("Bar Chart")
        fig = px.bar(df,x="LOGGER_NAME",y="PARA1_VAL")
        st.plotly_chart(fig,use_container_width=True,hight=200)
    if user==2.0:
        st.subheader("pie Chart")
        fig = px.pie(df,values="HOUR_VAL",names="LOGGER_NAME",hole=0.5)

        st.plotly_chart(fig,use_container_width=True,hight=200)

    if user==3.0:
        st.subheader("Line Chart")
        fig = px.line(df,x="HOUR_VAL",y="LOGGER_NAME")
        st.plotly_chart(fig,use_container_width=True,hight=200)

    else:
        st.warning("Upload csv file to see Analysis")

else:
    st.write("Enter valid Username and password")
