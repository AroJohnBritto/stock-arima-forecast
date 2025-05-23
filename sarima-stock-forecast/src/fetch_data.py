import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(symbol, start, end, output_path):
    data = yf.download(symbol, start=start, end=end)

    if not data.empty:
        data = data[["Close"]]
        data.reset_index(inplace=True)  # Ensure Date is a proper column
        data.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")
    else:
        print("No data downloaded. Check ticker and date range.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    fetch_stock_data("AAPL", "2014-01-01", "2024-12-31", "data/historical_data.csv")
# This script fetches historical stock data for Apple Inc. (AAPL) from Yahoo Finance
# and saves it to a CSV file. The data includes the closing prices from January 1, 2018,