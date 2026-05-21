import pandas as pd
from datetime import datetime, timezone

def transform_data(raw_records: list) -> pd.DataFrame:
    transformed_records = []
    for record in raw_records:
        transformed_records.append({
            "city":           record["name"],
            "country":        record["sys"]["country"],
            "temperature_c":  record["main"]["temp"],
            "feels_like_c":   record["main"]["feels_like"],
            "humidity_pct":   record["main"]["humidity"],
            "pressure_hpa":   record["main"]["pressure"],
            "wind_speed_ms":  record["wind"]["speed"],
            "weather_desc":   record["weather"][0]["description"],
            "extracted_at":   datetime.now(timezone.utc),
        })

    df = pd.DataFrame(transformed_records)    
    df = df.dropna(subset=["city", "temperature_c"])
    df["temperature_c"] = df["temperature_c"].round(2)
    df["humidity_pct"]  = df["humidity_pct"].clip(0, 100) 

    return df