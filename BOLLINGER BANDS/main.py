
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os


# Load and display the logo
logo_path = "IMAGE.png"
# Streamlit page configuration

st.title("BRAINS ADVISORY SERVICES")
st.image(logo_path, width=100)  # Adjust the width as needed
st.subheader("Technical Analysis")


# User Inputs
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Stock Ticker", value='AAPL')
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('2023-12-31'))

# Bollinger Bands Parameters
window_size = st.sidebar.number_input("Bollinger Bands Moving Average Window Size", min_value=1, value=20)
std_dev = st.sidebar.number_input("Bollinger Bands Standard Deviation", min_value=0.1, value=2.0)

# Fetch data from Yahoo Finance
@st.cache_resource
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

df = get_data(ticker, start_date, end_date)

# Calculate Bollinger Bands
df['MA'] = df['Close'].rolling(window=window_size).mean()
df['Upper Band'] = df['MA'] + (df['Close'].rolling(window=window_size).std() * std_dev)
df['Lower Band'] = df['MA'] - (df['Close'].rolling(window=window_size).std() * std_dev)

# Display last 5 trades
st.write("### Last 5 Trades")
st.dataframe(df.tail(5))

# Display dataframe description
st.write("### Dataframe Description")
st.table(df.describe())

# Plotting
st.write("### Stock Price with Bollinger Bands")
fig, ax = plt.subplots()
ax.plot(df['Close'], label='Close Price')
ax.plot(df['MA'], label='Moving Average')
ax.plot(df['Upper Band'], label='Upper Band', linestyle='--')
ax.plot(df['Lower Band'], label='Lower Band', linestyle='--')
ax.set_title(f"{ticker} Closing Price with Bollinger Bands")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
