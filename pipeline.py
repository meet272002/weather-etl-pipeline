from extract import extract_weather_data
from transform import transform_data
from load import load_data
from datetime import datetime

CITIES = ["Mumbai", "Delhi","Bangalore", "Hyderabad", "Ahmedabad"]

def run_pipeline():
    print(f"Pipeline Started at: {datetime.now()}")
    try:
        raw_data = extract_weather_data(CITIES)
        if not raw_data:
            print("No data extracted. Exiting pipeline.")
            return
        else:
            print(f"Extracted data for {len(raw_data)} cities.")
        clean = transform_data(raw_data)
        load_data(clean)
        print(f"Pipeline completed successfully at: {datetime.now()}")
    except Exception as e:
        print(f"Error during extraction: {e}")
        return