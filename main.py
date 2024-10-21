import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64
import io

# Function to fetch stock data
def get_stock_data(symbol, start_date, end_date):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(start=start_date, end=end_date)
        info = stock.info
        return hist, info
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {str(e)}")
        return None, None

# Function to create interactive price chart
def create_price_chart(data):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Price'
    ))
    fig.update_layout(
        title='Stock Price History',
        yaxis_title='Price',
        xaxis_title='Date',
        height=600,
        template='plotly_dark'
    )
    return fig

# Function to create download link for CSV
def get_csv_download_link(df, filename):
    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV File</a>'
    return href

# Main Streamlit app
def main():
    st.set_page_config(page_title="Stock Data Visualization", layout="wide")
    
    st.title("Stock Data Visualization App")
    
    # User input for stock symbol
    symbol = st.text_input("Enter stock symbol (e.g., AAPL for Apple):", "AAPL").upper()
    
    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", datetime.now() - timedelta(days=365))
    with col2:
        end_date = st.date_input("End date", datetime.now())
    
    if st.button("Fetch Data"):
        # Fetch stock data
        hist_data, info = get_stock_data(symbol, start_date, end_date)
        
        if hist_data is not None and info is not None:
            # Display key financial information
            st.subheader(f"Key Information for {symbol}")
            info_df = pd.DataFrame({
                "Metric": ["Company Name", "Sector", "Industry", "Market Cap", "Forward P/E", "Dividend Yield", "52 Week High", "52 Week Low"],
                "Value": [
                    info.get('longName', 'N/A'),
                    info.get('sector', 'N/A'),
                    info.get('industry', 'N/A'),
                    f"${info.get('marketCap', 0):,.0f}",
                    f"{info.get('forwardPE', 'N/A'):.2f}",
                    f"{info.get('dividendYield', 'N/A'):.2%}",
                    f"${info.get('fiftyTwoWeekHigh', 'N/A'):.2f}",
                    f"${info.get('fiftyTwoWeekLow', 'N/A'):.2f}"
                ]
            })
            st.table(info_df)
            
            # Display interactive price chart
            st.subheader(f"Stock Price History for {symbol}")
            price_chart = create_price_chart(hist_data)
            st.plotly_chart(price_chart, use_container_width=True)
            
            # Display recent data in a table
            st.subheader(f"Recent Stock Data for {symbol}")
            st.dataframe(hist_data.tail().style.format({
                'Open': '${:.2f}',
                'High': '${:.2f}',
                'Low': '${:.2f}',
                'Close': '${:.2f}',
                'Volume': '{:,.0f}'
            }))
            
            # Provide download link for CSV
            st.markdown(get_csv_download_link(hist_data, f"{symbol}_stock_data.csv"), unsafe_allow_html=True)
        else:
            st.warning("Failed to fetch data. Please check the stock symbol and try again.")

if __name__ == "__main__":
    main()
