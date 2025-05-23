import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_results(hist_path, forecast_path, output_path):
    df_hist = pd.read_csv(hist_path, parse_dates=["Date"])
    df_forecast = pd.read_csv(forecast_path)

    future_dates = pd.date_range(start=df_hist["Date"].iloc[-1] + pd.Timedelta(days=1), periods=len(df_forecast))
    df_forecast["Date"] = future_dates

    plt.figure(figsize=(12, 6))
    plt.plot(df_hist["Date"], df_hist["Close"], label="Historical")
    plt.plot(df_forecast["Date"], df_forecast["Forecast"], label="Forecast", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title("AAPL Stock Price Forecast (90 days)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    os.makedirs("plots", exist_ok=True)
    plot_results("data/cleaned_data.csv", "data/forecast.csv", "plots/forecast_plot.png")
