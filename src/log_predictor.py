# src/log_predictions.py
from sqlalchemy import create_engine
import logging

def log_predictions(df, server, user, password, database, table):
    try:
        conn_str = f"mysql+pymysql://{user}:{password}@{server}/{database}"
        engine = create_engine(conn_str)
        df.to_sql(table, engine, if_exists='replace', index=False)
        logging.info(f"Predictions stored to `{table}`.")
    except Exception as e:
        logging.error(f"Error logging predictions to SQL: {e}")
