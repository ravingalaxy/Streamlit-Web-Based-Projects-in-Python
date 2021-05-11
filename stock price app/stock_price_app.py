import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

shown are the stock **closing price** and **volume** of APPLE!

""")


tickerSymbol = 'AAPL'

tickerData =  yf.Ticker(tickerSymbol)

tickerDf =  tickerData.history(period = 'id', start = '2010-5-31', end = '2021-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
