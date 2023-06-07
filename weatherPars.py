import requests


def weather_forecast(city):
    params = {"lang": "ru",
              "M": "",
              "n": "",
              "q": "",
              "T": "",
              }
    url = f'https://wttr.in/{city}'

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

if __name__ == '__main__':
    print(weather_forecast("Лондон"))
    print(weather_forecast("Аэропорт Шереметьево"))
    print(weather_forecast("Череповец"))
