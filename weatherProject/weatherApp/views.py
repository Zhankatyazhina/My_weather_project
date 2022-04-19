from django.shortcuts import render


import urllib.request
import json


def index(request):
    if request.method== 'POST':
        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                      city + '&units=metric&appid=2fa4b033855d08d11cb55d72efc49e8d').read()
        list_of_data=json.loads(source)

        data={
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ','+str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) +'C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }

        print(data)
    else:
        data={}

    return render(request, "index.html" , data)