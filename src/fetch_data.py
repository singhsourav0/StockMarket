import yfinance as yf
import pandas as pd

def fetch_data():
    symbols = {'NIFTY': '^NSEI', 'SENSEX': '^BSESN'}

    for name, symbol in symbols.items():
        df = yf.download(symbol, start="2015-01-01", end="2024-01-01")
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        # df.drop(columns=['Index'], inplace=True)
        df.to_csv(f'Data/{name}_data.csv', index=False)

        print(f"Fetched data for {name} and saved to Data/{name}_data.csv")

        
if __name__ == "__main__":
    fetch_data()
        