 Weather App – Python & OpenWeatherMap API
This is a simple command-line weather application built using Python and the OpenWeatherMap API. It allows users to fetch real-time weather data (temperature, humidity, wind speed, and description) for any city in the world.

 Features
- Fetch current weather details by city name
- Displays:
  - Temperature (in Celsius)
  - Humidity
  - Wind speed
  - Weather description
- Error handling for invalid cities or API issues

 Tech Stack
- **Language**: Python
- **Library**: [`requests`](https://pypi.org/project/requests/)
- **API**: [OpenWeatherMap](https://openweathermap.org/api)

Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/palak-deep/weather-app.git
   cd weather-app
Install dependencies:                                                                                                                      
     -pip install requests

(Optional) Create and activate a virtual environment:                                                                                      
python -m venv venv                                                                                                                        
source venv/bin/activate    # On Windows: venv\Scripts\activate

Setup                                                                                                                                      
Get your API key from OpenWeatherMap.                                                                                                      
Replace the api_key value inside the script with your key:                                                                                 
api_key = "YOUR_API_KEY_HERE"                                                                                                               

Usage                                                                                                                                      
Run the script:                                                                                                                      python weather_app.py                                                                                                                      
You'll be prompted to enter the city name.                                                                                                 The app will display the current weather data for that city.

 License
This project is open-source and free to use for educational and personal purposes available under the MIT License.
