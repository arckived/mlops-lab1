import pytest

from src import converters, analyzer
from src.main import main


# ---------- Converter tests ----------

@pytest.mark.parametrize("c, f", [(0, 32.0), (100, 212.0), (-40, -40.0), (37, 98.6)])
def test_celsius_to_fahrenheit(c, f):
    assert converters.celsius_to_fahrenheit(c) == pytest.approx(f)


@pytest.mark.parametrize("f, c", [(32, 0.0), (212, 100.0)])
def test_fahrenheit_to_celsius(f, c):
    assert converters.fahrenheit_to_celsius(f) == pytest.approx(c)


def test_kmh_to_mph():
    assert converters.kmh_to_mph(100) == pytest.approx(62.14)


def test_negative_wind_raises():
    with pytest.raises(ValueError):
        converters.kmh_to_mph(-5)


def test_invalid_type_raises():
    with pytest.raises(TypeError):
        converters.celsius_to_fahrenheit("hot")


@pytest.mark.parametrize("temp, label", [(-5, "Freezing"), (5, "Cold"), (15, "Mild"), (25, "Warm"), (35, "Hot")])
def test_classify_temperature(temp, label):
    assert converters.classify_temperature(temp) == label


@pytest.mark.parametrize("speed, label", [(0, "Calm"), (10, "Light"), (30, "Moderate"), (50, "Strong"), (80, "Storm")])
def test_classify_wind(speed, label):
    assert converters.classify_wind(speed) == label


# ---------- Analyzer tests ----------

@pytest.fixture
def records():
    return analyzer.load_weather_data()


def test_data_loads(records):
    assert len(records) == 10


def test_get_cities(records):
    assert analyzer.get_cities(records) == ["Boston", "Miami"]


def test_average_temperature(records):
    assert analyzer.average(records, "temp_c", "Boston") == pytest.approx(4.0)
    assert analyzer.average(records, "temp_c", "Miami") == pytest.approx(25.0)
    assert analyzer.average(records, "temp_c") == pytest.approx(14.5)


def test_average_humidity_and_wind(records):
    assert analyzer.average(records, "humidity", "Boston") == pytest.approx(61.6)
    assert analyzer.average(records, "wind_kmh", "Miami") == pytest.approx(18.0)


def test_hottest_and_coldest(records):
    assert analyzer.hottest_day(records)["temp_c"] == 27.5
    assert analyzer.coldest_day(records)["date"] == "2025-01-02"
    assert analyzer.hottest_day(records, "Boston")["temp_c"] == 8.0


def test_unknown_city_raises(records):
    with pytest.raises(ValueError):
        analyzer.average(records, "temp_c", "Atlantis")


def test_city_summary(records):
    summary = analyzer.city_summary(records, "Boston")
    assert summary["avg_temp_f"] == pytest.approx(39.2)
    assert summary["category"] == "Cold"
    assert summary["days"] == 5


# ---------- App test ----------

def test_main_prints_report(capsys):
    main(["--city", "Miami"])
    output = capsys.readouterr().out
    assert "Weather report for Miami" in output
    assert "Warm" in output
