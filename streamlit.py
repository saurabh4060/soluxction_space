import streamlit as st
import plotly.express as px
import pandas as pd
import requests
import os #to navigate some file if needed
import warnings
warnings.filterwarnings('ignore')#to ignore warnings

st.set_page_config(page_title="Bank...",page_icon=":bar_chart",layout='wide')
st.title(" :bar_chart: Sample Superstore EDA")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    
else:
    url = "https://github.com/saurabh4060/soluxction_space/blob/main/Superstore.csv"

    # Download the file
    response = requests.get(url)
    if response.status_code == 200:
        with open("file.csv", "wb") as f:
            f.write(response.content)

    # Load the file into a DataFrame
    df = pd.read_csv("file.csv")

    st.error("Please upload a file.")



col1,col2 = st.columns((2))



df["Order Date"] = pd.to_datetime(df["Order Date"])    
         
startdate=pd.to_datetime(df["Order Date"]).min()

#max from above data
enddate=pd.to_datetime(df["Order Date"]).max()

with col1:
    date1=pd.to_datetime(st.date_input("Start date",startdate))
with col2:
    date2=pd.to_datetime(st.date_input("endt date",enddate))





df = df[(df["Order Date"]>= date1) & (df["Order Date"]<=date2)].copy()

#region
st.sidebar.header("Choose your filter :")
region= st.sidebar.multiselect("Pick your region ",df["Region"].unique())
if not region:
    df2=df.copy()
else:
    df2=df[df['Region'].isin(region)]
#state
state= st.sidebar.multiselect("Pick your state ",df2["State"].unique())
if not region:
    df3=df2.copy()
else:
    df3=df2[df2['State'].isin(state)]

#city
city= st.sidebar.multiselect("Pick your city ",df3['City'].unique())




if not state and not city and not region:
    filtered_df= df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]

elif not region and not city:
    filtered_df= df[df["State"].isin(state)]


elif state and city:
    filtered_df=df3[df["State"].isin(state) & df3["City"].isin(city) ]

elif region and city:
    filtered_df=df3[df["State"].isin(region) & df3["City"].isin(city) ]


elif region and state:
    filtered_df=df3[df["State"].isin(region) & df3["City"].isin(state) ]


elif city:
    filtered_df=df3["City"].isin(city)

else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]
    
category_df= filtered_df.groupby(by =['Category'],as_index=False)["Sales"].sum()


with col1:
    st.subheader("Category Wise Sales ")
    fig = px.bar( category_df,x="Category",y ="Sales")
    st.plotly_chart(fig,use_container_width=True,height= 200)

with col2:


    st.subheader("Region Wise Sales ")
    fig = px.pie( filtered_df,values="Sales",names="Region",hole=0.5)
    
    fig.update_traces(text = filtered_df["Region"],textposition="outside")
    st.plotly_chart(fig,use_container_width=True,height= 200)

