# app.py

import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

# Streamlit app title
st.title("Interactive Stock Data Visualization")

# Input field for the stock ticker (e.g., 'AAPL' for Apple)
ticker = st.text_input("Enter Stock Ticker:", "AAPL")

# Download stock data using yfinance
stock_data = yf.download(ticker, period="1y")

# Create a Plotly figure
fig = go.Figure()

# Add stock data (closing price) to the plot
fig.add_trace(go.Scatter(
    x=stock_data.index,
    y=stock_data['Close'],
    mode='lines',
    name=f'{ticker} Stock Price'
))

# Update layout of the figure
fig.update_layout(
    title=f'{ticker} Stock Price Over Last Year',
    xaxis_title='Date',
    yaxis_title='Closing Price (USD)',
    template="plotly_dark"
)

# Display the plot in Streamlit
st.plotly_chart(fig)

