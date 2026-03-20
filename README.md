# StockBriefs

A stock data visualization web application built with [Streamlit](https://streamlit.io/). StockBriefs lets you look up any publicly traded stock, explore its historical price data with interactive charts, view key financial metrics, and download data for further analysis.

## Features

- **Stock lookup** – Enter any ticker symbol (e.g. `AAPL`, `GOOGL`, `MSFT`) to pull live data from Yahoo Finance.
- **Date range selection** – Choose a custom start and end date (defaults to the past year).
- **Interactive candlestick chart** – Visualize Open / High / Low / Close prices with a dark-themed Plotly chart.
- **Key financial metrics** – Quickly see company name, sector, industry, market cap, P/E ratio, dividend yield, and 52-week high/low.
- **Recent data table** – Tabular view of the most recent OHLCV rows with formatted values.
- **CSV export** – Download the full historical dataset as a CSV file with one click.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python ≥ 3.11 |
| Web UI | [Streamlit](https://streamlit.io/) ≥ 1.39 |
| Data source | [yfinance](https://github.com/ranaroussi/yfinance) ≥ 0.2.46 |
| Charting | [Plotly](https://plotly.com/python/) ≥ 5.24 |
| Data wrangling | [Pandas](https://pandas.pydata.org/) ≥ 2.2, [NumPy](https://numpy.org/) ≥ 2.1 |
| Package manager | [uv](https://github.com/astral-sh/uv) |

## Getting Started

### Prerequisites

- Python 3.11 or newer
- [uv](https://github.com/astral-sh/uv) (recommended) **or** standard `pip`

### Installation

```bash
# Clone the repository
git clone https://github.com/highlanderkev/StockBriefs.git
cd StockBriefs

# Install dependencies with uv
uv sync

# — or — with pip
pip install streamlit>=1.39.0 yfinance>=0.2.46 pandas>=2.2.3 plotly>=5.24.1 numpy>=2.1.2
```

### Running the App

```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501` by default.

To run on a custom port (e.g. 5000):

```bash
streamlit run main.py --server.port 5000
```

## Usage

1. Enter a **stock ticker symbol** in the text field (e.g. `AAPL`).
2. Adjust the **start date** and **end date** as needed.
3. Click **Fetch Data**.
4. Explore the candlestick chart, financial metrics, and recent price table.
5. Click the **Download CSV** link to export the data locally.

## Project Structure

```
StockBriefs/
├── main.py              # Streamlit application
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Locked dependency versions
└── .streamlit/
    └── config.toml      # Streamlit server configuration
```

## License

License information for this project has not yet been specified. Until a license is added, all rights are reserved and you may not use, copy, modify, or distribute this code without explicit permission from the author.
