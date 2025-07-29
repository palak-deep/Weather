import requests

def get_weather(city):
    api_key = "d9cc345c632870bb35404fd5a40292aa"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Metric for Celsius

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Description: {description.capitalize()}")

        else:
            print(f"error")
    except Exception as e:
        print(f"Unable to fetch weather data: {e}")

def main():
    print("Welcome to the Weather App!")
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()