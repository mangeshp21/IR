import requests
import json

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] == 200:
            
            temperature = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            weather = data["weather"][0]["main"]

            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Description: {description}")
            print(f"Weather: {weather}")
        else:
            print("City not found")

    except Exception as e:
        print("An error occurred:", str(e))

api_key = "9dafa4d5ec2b4631fef59d925daa4543"
city_name = input("Enter Your City: ")  

get_weather(city_name, api_key)
