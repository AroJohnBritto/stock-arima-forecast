# stock-arima-forecast
# 📊 AAPL Stock Price Forecast using ARIMA

This project forecasts the next 90 trading days of Apple's daily closing price using a ARIMA time series model. The goal is to build a simple and interpretable pipeline that downloads historical stock data, processes it, fits a forecasting model, and visualizes the results.

## 🔧 Tools Used

- Python
- yfinance (for historical stock data)
- pandas, matplotlib
- pmdarima (for arima model)
- joblib (to save trained models)


## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
### 2. Run the pipeline
```
# Step 1: Download daily closing data for AAPL
python src/fetch_data.py

# Step 2: Clean the data
python src/etl_pipeline.py

# Step 3: Train arima and forecast 90 days
python src/forecast_arima.py

# Step 4: Plot the forecast as dots
python src/plot_forecast.py
```

### 3. Output
`data/forecast.csv` — contains 90 predicted prices

`models/arima_model.pkl` — saved model

`plots/forecast_plot.png` — chart of forecast (shown as dots, not a line)

### 🔎 Notes

- Forecasts are based on 5+ years of daily data.

- The model is retrained fresh each time for a clean workflow.

- You can change the stock ticker, time window, or model order in the scripts as needed.

## Author
Arockiyajohn Britto A
