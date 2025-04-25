# src/clean_data_sql.py
import mysql.connector
import logging

def clean_data_sql(host, user, password, database, table):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()
        
        # Round values of Close, High, Low, and Open columns to 2 decimal places
        cursor.execute(f"""
            UPDATE {table}
            SET Close = ROUND(Close, 2),
                High = ROUND(High, 2),
                Low = ROUND(Low, 2),
                Open = ROUND(Open, 2)
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Data cleaned in SQL.")
    except Exception as e:
        logging.error(f"Error cleaning data in SQL: {e}")
