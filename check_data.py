import sqlite3
import pandas as pd
import os

DB_Path = os.getenv("DB_PATH", "weather_data.db")

def get_data():
    conn = sqlite3.connect(DB_Path)
    try:
        query = "SELECT * FROM weather_readings"
        df = pd.read_sql_query(query, conn)
        print(df)
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

if __name__ == "__main__":
    get_data()