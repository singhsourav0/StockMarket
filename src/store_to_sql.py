# src/store_to_sql.py
import mysql.connector
import logging

def store_to_sql(df, host, user, password, database, table):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'  # In case you hit auth issues
        )
        cursor = conn.cursor()

        # Drop the table if it already exists
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

        # Dynamically create table based on DataFrame
        columns = ", ".join([f"`{col}` TEXT" for col in df.columns])  # Storing all as TEXT for simplicity
        cursor.execute(f"CREATE TABLE {table} ({columns})")

        # Insert data
        for _, row in df.iterrows():
            placeholders = ", ".join(["%s"] * len(row))
            sql = f"INSERT INTO {table} VALUES ({placeholders})"
            cursor.execute(sql, tuple(row.astype(str)))  # Convert all to str for TEXT columns

        conn.commit()
        logging.info(f"Data stored to table `{table}` in `{database}`.")
        cursor.close()
        conn.close()

    except Exception as e:
        logging.error(f"Error storing data to SQL: {e}")
