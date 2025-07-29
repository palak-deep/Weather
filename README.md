Weather App

Overview:
This project is a simple Python-based command-line application that fetches real-time weather information for any city using the OpenWeatherMap API. It displays key weather parameters like temperature, humidity, wind speed, and weather conditions in an easy-to-read format.

Features:
Fetches current weather data from OpenWeatherMap API.
Displays temperature in Celsius, humidity percentage, wind speed in km/h, and weather description.
Handles errors gracefully, such as invalid city names or network issues.
Lightweight and easy-to-use command-line interface.

Technologies Used:
Python: Core programming language.
Requests: For making HTTP requests to the weather API.
OpenWeatherMap API: Provides reliable real-time weather data.

How It Works:
The user inputs a city name.
The app sends a request to the OpenWeatherMap API with the city name and API key.
The API returns current weather data in JSON format.
The app parses this data and displays temperature, humidity, wind speed, and a brief weather description.
If the city is not found or an error occurs, the app notifies the user.

Usage:
Run the Python script.
When prompted, enter the city name.
View the displayed weather information in the terminal.

Future Improvements:
Add support for extended forecasts (daily/weekly weather).
Implement a GUI using frameworks like Tkinter or Streamlit.
Allow temperature unit selection (Celsius, Fahrenheit).
Cache recent queries to reduce API calls and improve speed.

