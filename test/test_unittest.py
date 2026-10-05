import unittest

from src import converters, analyzer


class TestConverters(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(converters.celsius_to_fahrenheit(100), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(converters.fahrenheit_to_celsius(32), 0.0)

    def test_kmh_to_mph(self):
        self.assertAlmostEqual(converters.kmh_to_mph(100), 62.14)

    def test_negative_wind(self):
        with self.assertRaises(ValueError):
            converters.classify_wind(-1)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            converters.kmh_to_mph(None)

    def test_classify_temperature(self):
        self.assertEqual(converters.classify_temperature(-3), "Freezing")
        self.assertEqual(converters.classify_temperature(31), "Hot")


class TestAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.records = analyzer.load_weather_data()

    def test_record_count(self):
        self.assertEqual(len(self.records), 10)

    def test_cities(self):
        self.assertEqual(analyzer.get_cities(self.records), ["Boston", "Miami"])

    def test_city_average(self):
        self.assertAlmostEqual(analyzer.average(self.records, "temp_c", "Miami"), 25.0)

    def test_hottest_day(self):
        self.assertEqual(analyzer.hottest_day(self.records)["date"], "2025-01-04")

    def test_summary(self):
        summary = analyzer.city_summary(self.records, "Miami")
        self.assertEqual(summary["category"], "Warm")
        self.assertAlmostEqual(summary["avg_temp_f"], 77.0)


if __name__ == "__main__":
    unittest.main()
