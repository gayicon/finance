import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

# Streamlit app title
st.title("Stock Price Movements for the Last 365 Days")

# Input field for stock ticker symbol
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL for Apple):", "AAPL")

# Fetch the stock data for the last 365 days
stock_data = yf.download(ticker, period="1y", interval="1d")

# Check if data is available for the ticker
if stock_data.empty:
    st.write(f"Sorry, no data found for the ticker symbol {ticker}. Please try again with a valid symbol.")
else:
    # Create a Plotly figure
    fig = go.Figure()

    # Add the stock data (closing price) to the plot
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['Close'],
        mode='lines',
        name=f'{ticker} Stock Price'
    ))

    # Update layout of the figure
    fig.update_layout(
        title=f'{ticker} Stock Price Movements Over the Last 365 Days',
        xaxis_title='Date',
        yaxis_title='Closing Price (USD)',
        template="plotly_dark",
        xaxis_rangeslider_visible=True
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)
