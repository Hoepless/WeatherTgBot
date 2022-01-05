import requests
from pprint import pprint
from config import open_weather_token
from datetime import datetime

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Rain \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Чел выгляни в окно"

        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Weather in: {city}\nTemperature: {cur_weather}C° {wd}\n"
              f"Humidity: {humidity}%\nWind: {wind} m/s\n"
              "Have a good day abai!"
              )

    except Exception as e:
        print(e)
        print("Check city name")

def main():
    city = input("Enter city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()