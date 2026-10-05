# mlops-lab1
# Weather Analytics App 

A Python command line application that analyzes weather data and generates city weather reports, with automated testing through GitHub Actions.

## Features
* Loads weather data (temperature, humidity and wind speed) from a CSV dataset
* Converts temperatures between Celsius and Fahrenheit, and wind speed from km/h to mph
* Classifies temperatures (Freezing, Cold, Mild, Warm, Hot) and wind levels (Calm, Light, Moderate, Strong, Storm)
* Computes per city averages and finds the hottest and coldest days
* Prints a formatted weather report for all cities or a single city
* Validates input and raises clear errors for invalid values

## Dataset
data/weather.csv contains five days of weather readings for Boston and Miami with the columns date, city, temp_c, humidity and wind_kmh.

