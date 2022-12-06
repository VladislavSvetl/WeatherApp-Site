from django.shortcuts import render
import requests


def index(request):
    appid = "c285d41d09ba722c41714e9e75753558"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=" + appid

    city = 'London'

    return render(request, 'Weather/index.html')
