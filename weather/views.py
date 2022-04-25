import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'c9632f3223ad6db342a9cf1a41c5160c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                'error': False,
            }
            if city_info not in all_cities:
                all_cities.append(city_info)
        else:
            city_info = {
                'city': city.name,
                'error': True
            }
            print('город не существует')
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
