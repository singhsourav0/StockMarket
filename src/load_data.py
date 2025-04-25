# src/load_data.py
import mysql.connector
import pandas as pd
import logging

def load_from_sql(host, user, password, database, table):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

        logging.info(f"Loaded {len(df)} rows from `{table}`.")
        cursor.close()
        conn.close()
        return df

    except mysql.connector.Error as e:
        logging.error(f"Error loading data from SQL: {e}")
        return pd.DataFrame()

