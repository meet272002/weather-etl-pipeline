import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OW_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad"]

# Created by Meet Gandhi on 2024-06-01
# Function to extract weather data for a list of cities
def extract_weather_data(cities: list) -> list:
    raw_records = []
    for city in cities:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL,params=params,timeout=10)
        response.raise_for_status()
        raw_records.append(response.json())
        print(f"Data extracted for {city}")
    return raw_records