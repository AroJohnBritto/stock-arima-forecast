import pandas as pd
import pmdarima as pm
import joblib
import os

def run_forecast(data_path, steps, model_path, forecast_path):
    df = pd.read_csv(data_path, parse_dates=["Date"])
    y = df["Close"]

    model = pm.auto_arima(y, seasonal=False, stepwise=True, suppress_warnings=True)
    forecast = model.predict(n_periods=steps)

    joblib.dump(model, model_path)
    pd.DataFrame({"Forecast": forecast}).to_csv(forecast_path, index=False)

    print("Model and forecast saved.")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    run_forecast(
        "data/cleaned_data.csv",
        steps=90,
        model_path="models/arima_model.pkl",
        forecast_path="data/forecast.csv"
    )
