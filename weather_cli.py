import json
import requests

def load_language(lang):
    try:
        with open(f"locales/{lang}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Language file not found. Defaulting to English.")
        with open("locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

lang = input("Choose language (en/th): ").strip().lower()
messages = load_language(lang)

print(messages["welcome"])
city = input(messages["enter_city"])
print(messages["selected_city"].format(city=city))

def get_weather(city):
    api_key = "YOUR_API_KEY" # Replace with your OpenWeatherMap API key 
    base_url = "http://api.openweathermap.org/data/2.5/weather" # API endpoint 
    response = requests.get(base_url, params={"q": city, "appid": api_key, "units": "metric"})
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return messages["weather_success"].format(city=city, weather=weather, temperature=temperature)
    else:
        return messages["weather_error"].format(city=city)

weather_info = get_weather(city)
print(weather_info)
