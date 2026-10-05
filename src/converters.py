

"""Unit conversions and weather classifications."""


def _check_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")


def celsius_to_fahrenheit(temp_c):
    _check_number(temp_c)
    return round(temp_c * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(temp_f):
    _check_number(temp_f)
    return round((temp_f - 32) * 5 / 9, 2)


def kmh_to_mph(speed_kmh):
    _check_number(speed_kmh)
    if speed_kmh < 0:
        raise ValueError("Wind speed cannot be negative")
    return round(speed_kmh * 0.621371, 2)


def classify_temperature(temp_c):
    _check_number(temp_c)
    if temp_c < 0:
        return "Freezing"
    if temp_c < 10:
        return "Cold"
    if temp_c < 20:
        return "Mild"
    if temp_c < 30:
        return "Warm"
    return "Hot"


def classify_wind(speed_kmh):
    _check_number(speed_kmh)
    if speed_kmh < 0:
        raise ValueError("Wind speed cannot be negative")
    if speed_kmh < 1:
        return "Calm"
    if speed_kmh < 20:
        return "Light"
    if speed_kmh < 40:
        return "Moderate"
    if speed_kmh < 62:
        return "Strong"
    return "Storm"
