# new_project_file_trial.py

import yfinance as yf
import streamlit as st

def get_ticker_data(ticker):
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period="1mo")
    info = ticker_obj.info
    return data, info

# Streamlit dashboard
st.title("Stock Dashboard")
ticker = st.text_input("Enter Ticker Symbol (e.g., AAPL, MSFT):", "AAPL")

if ticker:
    data, info = get_ticker_data(ticker)
    st.subheader(f"{info.get('shortName', ticker)} ({ticker})")
    st.write("**Sector:**", info.get('sector', 'N/A'))
    st.write("**Market Cap:**", info.get('marketCap', 'N/A'))
    st.write("**Previous Close:**", info.get('previousClose', 'N/A'))
    st.write("**Open:**", info.get('open', 'N/A'))
    st.write("**52 Week High:**", info.get('fiftyTwoWeekHigh', 'N/A'))
    st.write("**52 Week Low:**", info.get('fiftyTwoWeekLow', 'N/A'))
    st.line_chart(data['Close'])

