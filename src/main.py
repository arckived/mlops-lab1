"""Command line Weather Analytics app.

Usage (from the repo root):
    python -m src.main
    python -m src.main --city Boston
"""

import argparse

from src.analyzer import load_weather_data, get_cities, city_summary
from src.converters import classify_wind


def format_report(summary):
    lines = [
        f"Weather report for {summary['city']} ({summary['days']} days)",
        f"  Average temperature: {summary['avg_temp_c']} C / {summary['avg_temp_f']} F ({summary['category']})",
        f"  Average humidity:    {summary['avg_humidity']}%",
        f"  Average wind speed:  {summary['avg_wind_kmh']} km/h ({classify_wind(summary['avg_wind_kmh'])})",
        f"  Hottest day:         {summary['hottest'][0]} at {summary['hottest'][1]} C",
        f"  Coldest day:         {summary['coldest'][0]} at {summary['coldest'][1]} C",
    ]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Weather Analytics Report")
    parser.add_argument("--city", help="City to report on (default: all cities)")
    args = parser.parse_args(argv)

    records = load_weather_data()
    cities = [args.city] if args.city else get_cities(records)
    for city in cities:
        print(format_report(city_summary(records, city)))
        print()


if __name__ == "__main__":
    main()
