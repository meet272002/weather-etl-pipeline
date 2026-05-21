# weather-etl-pipeline

A beginner-friendly ETL pipeline built with Python that extracts live weather data from the OpenWeather API across multiple Indian cities, transforms and validates it using Pandas, and loads it incrementally into a SQLite database on an automated 30-minute schedule.

---

## Overview

This project demonstrates core Data Engineering concepts through a real, working pipeline:

- **Extract** — Fetches live weather data from the OpenWeather API for multiple cities
- **Transform** — Cleans, validates, and reshapes raw JSON into structured tabular data using Pandas
- **Load** — Appends clean records incrementally into a local SQLite database
- **Schedule** — Runs the full pipeline automatically every 30 minutes

---

## Project Structure

```
weather-etl-pipeline/
├── .env                  # API key + config (never commit this)
├── .gitignore
├── requirements.txt
├── extract.py            # Fetches raw JSON from OpenWeather API
├── transform.py          # Cleans and reshapes data with Pandas
├── load.py               # Loads DataFrame into SQLite
├── pipeline.py           # Orchestrates extract → transform → load
├── scheduler.py          # Runs pipeline on a 30-minute schedule
├── check_db.py           # Utility script to inspect loaded data
└── weather_etl.db        # Auto-created SQLite database (gitignored)
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| `requests` | HTTP calls to OpenWeather API |
| `pandas` | Data transformation and validation |
| `sqlite3` | Local database storage (built into Python) |
| `python-dotenv` | Manage environment variables |
| `schedule` | Automated 30-minute pipeline runs |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-etl-pipeline.git
cd weather-etl-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get your OpenWeather API key

Sign up at [openweathermap.org](https://openweathermap.org/api) and grab your free API key. Note: new keys take up to 10 minutes to activate.

### 4. Create your `.env` file

```bash
OW_API_KEY=your_api_key_here
SQLITE_DB_PATH=weather_etl.db
```

### 5. Run the pipeline once

```bash
python pipeline.py
```

### 6. Start the scheduler (runs every 30 minutes)

```bash
python scheduler.py
```

---

## Verify the Data

After running the pipeline, inspect what was loaded:

```bash
python check_db.py
```

This prints a full report including row count, per-city summary, latest records, and data quality checks.

Or query directly in Python:

```python
import sqlite3, pandas as pd

conn = sqlite3.connect("weather_etl.db")
df   = pd.read_sql("SELECT * FROM weather_readings ORDER BY extracted_at DESC", conn)
print(df.head())
conn.close()
```

---

## Sample Output

```
city       temperature_c  humidity_pct  weather_desc     extracted_at
Mumbai          29.4            78      broken clouds    2025-05-21 10:30:00
Delhi           38.1            22      clear sky        2025-05-21 10:30:00
Bangalore       24.7            65      few clouds       2025-05-21 10:30:00
Vadodara        37.2            18      clear sky        2025-05-21 10:30:00
Chennai         31.6            80      light rain       2025-05-21 10:30:00
```

---

## Data Schema

Table: `weather_readings`

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Auto-incremented primary key |
| `city` | TEXT | City name |
| `country` | TEXT | ISO country code |
| `temperature_c` | REAL | Temperature in °C |
| `feels_like_c` | REAL | Perceived temperature in °C |
| `humidity_pct` | INTEGER | Relative humidity (0–100%) |
| `pressure_hpa` | INTEGER | Atmospheric pressure in hPa |
| `wind_speed_ms` | REAL | Wind speed in m/s |
| `weather_desc` | TEXT | Sky condition description |
| `extracted_at` | TEXT | UTC timestamp of extraction |

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `OW_API_KEY` | — | Your OpenWeather API key (required) |
| `SQLITE_DB_PATH` | `weather_etl.db` | Path to the SQLite database file |

To change the cities tracked, edit the `CITIES` list in `pipeline.py`:

```python
CITIES = ["Mumbai", "Delhi", "Bangalore", "Vadodara", "Chennai"]
```

To change the schedule interval, edit `scheduler.py`:

```python
schedule.every(30).minutes.do(run_pipeline)  # change 30 to any value
```

---

## Error Handling

The pipeline is designed to fail gracefully:

- If one city's API call fails (timeout, invalid name, rate limit), that city is skipped and the rest continue
- All errors are logged with timestamps to the console
- Failed runs do not corrupt existing data in the database

---

## Author

**Meet Gandhi** — MSc Data Science, Dhirubhai Ambani University
[LinkedIn](https://linkedin.com/in/meetgandhi) · [GitHub](https://github.com/meet)
