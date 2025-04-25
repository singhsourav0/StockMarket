# src/main_pipeline.py
from src.fetch_data import fetch_data
from src.store_to_sql import store_to_sql
from src.clean_data_sql import clean_data_sql
from src.load_data import load_from_sql
from src.feature_engineering import add_features
import logging
import pandas as pd
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data_file, raw_table, host, user, password, database):
    if os.path.exists(data_file):
        logging.info(f"Loading data from file: {data_file}")
        data = pd.read_csv(data_file)
    else:
        logging.info(f"Data file {data_file} not found. Fetching data using fetch_data.")
        data = fetch_data()
        if data is not None and not data.empty:
            data.to_csv(data_file, index=False)
            logging.info(f"Fetched data saved to file: {data_file}")
        else:
            logging.error("Data fetching failed or returned invalid data.")
            data = pd.DataFrame()
    if not data.empty:
        store_to_sql(data, host, user, password, database, raw_table)
        clean_data_sql(host, user, password, database, raw_table)
        cleaned = load_from_sql(host, user, password, database, raw_table)
        if not cleaned.empty:
            featured = add_features(cleaned)
            print(f"Processed data for table {raw_table}:")
            print(featured.head())

if __name__ == "__main__":
    host = "127.0.0.1"
    user = "root"
    password = "**********"
    database = "stocksql"
    auth_plugin = 'mysql_native_password'

    # Process NIFTY data
    nifty_data_file = 'Data/NIFTY_data.csv'
    nifty_raw_table = 'stock_nifty'
    process_data(nifty_data_file, nifty_raw_table, host, user, password, database)

    # Process SENSEX data
    sensex_data_file = 'Data/SENSEX_data.csv'
    sensex_raw_table = 'stock_sensex'
    process_data(sensex_data_file, sensex_raw_table, host, user, password, database)
