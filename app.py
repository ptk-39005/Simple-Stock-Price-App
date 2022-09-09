from tokenize import String

import yfinance as yf
import streamlit as st
import datetime as dt

endDate = dt.datetime.now()

st.set_page_config("""Simple Stock Price App""")

st.write(""" # Simple Stock Price App """)




title = st.text_input('Enter Stock Code of the Company ', '')
tickerSymbol = title


if title:
    st.write("""

 Shown are the stock closing **Price** and **Volume** of the Entered Company : 
"""
)






#define the ticker symbol

#get data on this ticker
if title:
    st.write("""
    ## Closing Price :
    """)


tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=endDate)



st.line_chart(tickerDf.Close)
if title:
    st.write("""
    ## Volume Price :
    """)

st.line_chart(tickerDf.Volume)