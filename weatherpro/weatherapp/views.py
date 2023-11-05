from django.shortcuts import render
from decouple import config
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amsterdam'

    # appid = '19a8a274feb9e734e9d7bc76594478b6'
    appid = config('OPEN_WEATHER_API_KEY') 
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'city','appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    return render(request,
                  'weatherapp/index.html', {
                      'description': description,
                      'icon': icon,
                      'temp': temp,
                      'day': day,
                      'city': city,
                      }
                )