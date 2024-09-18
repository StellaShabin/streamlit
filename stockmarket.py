import streamlit as st
import yfinance as yf
import datetime

title = st.text_input("Ticker symbol", "MSFT")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("start date:",datetime.date(2014, 7, 6))

with col2:
    end_date = st.date_input("End date:", datetime.date(2024, 7, 6))
data=yf.download(title,start=start_date,end=end_date)
st.write(data)
st.line_chart(data['Close'])
