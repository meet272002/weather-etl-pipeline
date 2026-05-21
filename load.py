import sqlite3
import pandas as pd
import os
import logging
from datetime import datetime

log = logging.getLogger(__name__)

DB_Path = os.getenv("DB_PATH", "weather_data.db")

def get_connection():
    conn = sqlite3.connect(DB_Path)
    return conn

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS weather_readings(
                 id            INTEGER PRIMARY KEY AUTOINCREMENT,
                city          TEXT,
                country       TEXT,
                temperature_c REAL,
                feels_like_c  REAL,
                humidity_pct  INTEGER,
                pressure_hpa  INTEGER,
                wind_speed_ms REAL,
                weather_desc  TEXT,
                extracted_at  TEXT
                )"""
            )
    conn.commit()

def load_data(df: pd.DataFrame):
    conn = get_connection()
    try:
        create_table(conn)
        df["extracted_at"] = df["extracted_at"].astype(str)
        df.to_sql(name="weather_readings", con=conn, if_exists="append", index=False)
        log.info("Loaded %d rows into SQLite (%s)", len(df), DB_Path)
    except Exception as e:
        log.error("Error occurred while loading data: %s", str(e))
    finally:
        conn.close()