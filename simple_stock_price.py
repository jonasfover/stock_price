import yfinance as yf
import streamlit as st
import pandas as pd 
import datetime

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")
timestamp = pd.Timestamp(datetime.datetime(2021, 10, 10))

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

res = timestamp.today()

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=res)

# Open	High	Low	Close	Volume	Dividends	Stock Splits

# see your data
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)






