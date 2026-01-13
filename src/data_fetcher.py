import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, start_date="2015-01-01"):
    """
    Fetch historical stock data using Yahoo Finance
    """
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date)

    df.reset_index(inplace=True)
    df["Ticker"] = ticker
    return df


if __name__ == "__main__":
    tickers = ["NVDA", "NFLX"]
    all_data = []

    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_stock_data(ticker)
        all_data.append(data)

    final_df = pd.concat(all_data, ignore_index=True)

    today = datetime.today().strftime("%Y-%m-%d")
    file_path = f"data/raw/stock_data_{today}.csv"

    final_df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

