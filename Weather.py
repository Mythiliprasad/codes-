import requests

API_KEY = "YOUR_API_KEY_HERE" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"☁️ Weather: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("\n❌ City not found or API error!")

if __name__ == "__main__":
    print("== Weather App ==")
    city_name = input("Enter city name: ")
    get_weather(city_name)
