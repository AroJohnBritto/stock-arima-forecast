import pandas as pd

def clean_data(path):
    df = pd.read_csv("data/historical_data.csv", index_col=0, parse_dates=True)
    df.reset_index(inplace=True)
    df.dropna(inplace=True)
    df.sort_values("Date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

if __name__ == "__main__":
    df_clean = clean_data("data/historical_data.csv")
    df_clean.to_csv("data/cleaned_data.csv", index=False)
    print("Cleaned data saved.")
