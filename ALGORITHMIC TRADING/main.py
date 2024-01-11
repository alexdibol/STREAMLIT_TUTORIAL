import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Function to get data and calculate SMA
def get_data_with_sma(ticker, start_date, end_date, short_sma, long_sma):
    df = yf.download(ticker, start=start_date, end=end_date)
    df['Short_SMA'] = df['Close'].rolling(window=short_sma).mean()
    df['Long_SMA'] = df['Close'].rolling(window=long_sma).mean()
    return df


# Function to generate buy and sell signals
def generate_signals(df, short_sma, long_sma):
    df['Signal'] = 0
    df['Signal'][short_sma:] = np.where(df['Short_SMA'][short_sma:] > df['Long_SMA'][short_sma:], 1, 0)
    df['Position'] = df['Signal'].diff()


# Function to plot data and signals
def plot_data_and_signals(df):
    buy_signals = df[df['Position'] == 1]
    sell_signals = df[df['Position'] == -1]

    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], color='black', label='Stock Price')
    plt.plot(df['Short_SMA'], color='blue', label='Short SMA')
    plt.plot(df['Long_SMA'], color='magenta', label='Long SMA')

    plt.scatter(buy_signals.index, df['Close'][buy_signals.index], marker='^', color='green', label='Buy Signal',
                alpha=1)
    plt.scatter(sell_signals.index, df['Close'][sell_signals.index], marker='v', color='red', label='Sell Signal',
                alpha=1)

    plt.title(f'Stock Price and SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    return plt


# Streamlit interface
st.title('SMA Trading Strategy Visualization')

# Inputs
ticker = st.text_input('Enter Stock Ticker (e.g. AAPL)', 'AAPL')
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')
short_sma = st.number_input('Short SMA Window', min_value=1, value=20)
long_sma = st.number_input('Long SMA Window', min_value=1, value=50)

if st.button('Generate Chart'):
    df = get_data_with_sma(ticker, start_date, end_date, short_sma, long_sma)
    generate_signals(df, short_sma, long_sma)
    fig = plot_data_and_signals(df)
    st.pyplot(fig)
