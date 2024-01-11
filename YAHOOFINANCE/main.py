import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit page configuration
st.set_page_config(page_title="Financial Data Plotter", layout="wide")

# Title
st.title("Financial Data Plotter")

# User Inputs
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Stock Ticker", value='AAPL')
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('2023-12-31'))

# Fetch data from Yahoo Finance
@st.cache_resource
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

df = get_data(ticker, start_date, end_date)

# Display last 5 trades
st.write("### Last 5 Trades")
st.dataframe(df.tail(5))

# Display dataframe description
st.write("### Dataframe Description")
st.table(df.describe())

# Plotting
st.write("### Stock Price Time Series Plot")
fig, ax = plt.subplots()
ax.plot(df['Close'])
ax.set_title(f"{ticker} Closing Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
st.pyplot(fig)
