import requests
import json

def get_wheater(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    response = requests.get(complete_url)
    return response.json()

def display_weather(data):
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]

        print(f"Temperature: {temperature}k")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
        else:
        print("City not found!")

def main():
    api_key = "YOUR API KEY HERE" #Replace with your api key HERE
    city_name = input("Enter city name: ")
    weather_data = get_wheater(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()