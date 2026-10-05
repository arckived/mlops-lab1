
"""Load and analyze the weather dataset."""

import csv
from pathlib import Path

from src.converters import celsius_to_fahrenheit, classify_temperature

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "weather.csv"


def load_weather_data(path=DATA_PATH):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return [
            {
                "date": row["date"],
                "city": row["city"],
                "temp_c": float(row["temp_c"]),
                "humidity": float(row["humidity"]),
                "wind_kmh": float(row["wind_kmh"]),
            }
            for row in reader
        ]


def get_cities(records):
    return sorted({r["city"] for r in records})


def filter_by_city(records, city=None):
    if city is None:
        selected = list(records)
    else:
        selected = [r for r in records if r["city"] == city]
    if not selected:
        raise ValueError(f"No records found for city: {city}")
    return selected


def average(records, field, city=None):
    values = [r[field] for r in filter_by_city(records, city)]
    return round(sum(values) / len(values), 2)


def hottest_day(records, city=None):
    return max(filter_by_city(records, city), key=lambda r: r["temp_c"])


def coldest_day(records, city=None):
    return min(filter_by_city(records, city), key=lambda r: r["temp_c"])


def city_summary(records, city):
    avg_temp = average(records, "temp_c", city)
    hottest = hottest_day(records, city)
    coldest = coldest_day(records, city)
    return {
        "city": city,
        "days": len(filter_by_city(records, city)),
        "avg_temp_c": avg_temp,
        "avg_temp_f": celsius_to_fahrenheit(avg_temp),
        "avg_humidity": average(records, "humidity", city),
        "avg_wind_kmh": average(records, "wind_kmh", city),
        "hottest": (hottest["date"], hottest["temp_c"]),
        "coldest": (coldest["date"], coldest["temp_c"]),
        "category": classify_temperature(avg_temp),
    }
