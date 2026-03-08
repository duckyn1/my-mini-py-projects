import requests
import time

t = time.localtime()
current = time.strftime("%H:%M:%S", t)

api_key = "" # enter YOUR api key :(
city = input("Enter your city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"\n Weather in {city}. (Today is {current}):")
        print(f"Temp: {temp}°C (feels like {feels_like}°C)")
        print(f"Outside: {desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} m/s")

    elif response.status_code == 404:
        print("This city doesn't exist.")
    else:
        print("Error of API.")
except Exception as e:
    print(f"Error: {e}")