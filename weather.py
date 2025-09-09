import requests

API_KEY = "https://api.open-meteo.com/v1/forecast?latitude=42.6667&longitude=25.25&hourly=temperature_2m"
BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=42.6667&longitude=25.25&hourly=temperature_2m"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        
        print(f"Current temperature in {city} is {temp}°C with {description}.")
    else:
        print("City not found.")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
        