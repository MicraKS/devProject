import requests


def give_weather(city):
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
    places = ["Лондон", "SVO", "Череповец"]
    for place in places:
        print(give_weather(place))
