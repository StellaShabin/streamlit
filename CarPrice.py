import pandas as pd
import streamlit as st
from datetime import time
import pickle
st.header("Cars24 Used Car price prediction", divider="gray")
doc=pd.read_csv('https://docs.google.com/spreadsheets/d/1RX5WSYXK69ZLYDp8J5TgxV8DZPL5LMQpdNByPFnQtRM/export?format=csv&gid=2141295606')
st.write(doc.head())
col1,col2=st.columns(2)
with col1:
    option1 = st.selectbox("Select the fuel type:",("Diesel", "Petrol", "CNG", "LPG","Electric"),)
    option3 = st.selectbox("Select the transmission type:",("Automatic", "Manual"))
with col2:
    option2 = st.slider("Set the engine power:", 0, 130, 25)
    option4 = st.selectbox("Select the number of seats:",(4,5,7,9,11))
encode_dict={"option1":{"Diesel": 1, "Petrol": 2,"CNG": 3,"LPG": 4,"Electric": 5},
             "option3":{"Automatic": 1 ,"Manual": 2},
             "seller_type":{"Dealer": 1,"Individual": 2,"Trustmark Dealer": 3}}
def model_pred(option1,option3,option2,option4):
    with open('car_pred','rb') as file:
        reg_model=pickle.load(file)
        input_features=[[2018,1,4000,option1,option3,19.70,option2,86.30,option4]]
        return reg_model.predict(input_features)
if st.button("Submit"):
    option1=encode_dict["option1"][option1]
    option3=encode_dict["option3"][option3]
    price=model_pred(option1,option3,option2,option4)
    st.write("The price of the car is:", round(price.item(),2))
    
