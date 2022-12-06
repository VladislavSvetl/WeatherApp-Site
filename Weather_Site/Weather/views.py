from django.shortcuts import render
import requests


def index(request):
    appid = "c285d41d09ba722c41714e9e75753558"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    print(res)

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'humidity': res['main']['humidity'],
        'feels': res['main']['feels_like'],
        'wind_speed': res['wind']['speed'],
        'icon': res['weather'][0]['icon']
    }

    context = {'info': city_info}

    return render(request, 'Weather/index.html', context)
