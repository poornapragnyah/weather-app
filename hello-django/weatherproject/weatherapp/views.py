from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Bangalore'
    k = []
    g = [] 
    appid = '8ee4a2adb8cc5ec444247d6466e35a12'
    URL = "https://api.openweathermap.org/data/2.5/weather?"
    PARAMS = {'q': city, 'appid' : appid, 'units' : 'metric'}
    r = requests.get(url = URL, params=PARAMS)
    res = r.json()
    lat = res['coord']['lat']
    lon = res['coord']['lon']
    URL2 = 'https://api.openweathermap.org/data/2.5/forecast?'
    PARAMS2 = {'q': city, 'appid' : appid, 'lat': lat, 'lon': lon, 'units' : 'metric'}
    s = requests.get(url = URL2, params=PARAMS2)
    res2 = s.json()
    res2list = res2['list']
    day = datetime.date.today()
    for i in range(1, 6):
        g.append((day + datetime.timedelta(days=i)).strftime('%d-%m-%Y'))
    for i in range(5):
        k.append([res2list[i]['main']['temp'], res2list[i]['weather'][0]['description'], res2list[i]['weather'][0]['icon'], g[i]])


    day1temp = k[0][0]
    day2temp = k[1][0]
    day3temp = k[2][0]
    day4temp = k[3][0]
    day5temp = k[4][0]

    day1desc = k[0][1]
    day2desc = k[1][1]
    day3desc = k[2][1]
    day4desc = k[3][1]
    day5desc = k[4][1]

    day1icon = k[0][2]
    day2icon = k[1][2]
    day3icon = k[2][2]
    day4icon = k[3][2]
    day5icon = k[4][2]

    day1date = g[0]
    day2date = g[1]
    day3date = g[2]
    day4date = g[3]
    day5date = g[4]


    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    feels_like = res['main']['feels_like']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind_speed = res['wind']['speed']
    return render(request, 'weatherapp/index.html', {'description' : description, 'icon' : icon, 'temp' : temp, 'day' : day, 'city': city, 'feels_like' : feels_like, 'pressure':pressure, 'wind_speed':wind_speed, 'humidity':humidity, '5day': k,
    'day1temp': day1temp, 'day2temp': day2temp, 'day3temp': day3temp, 'day4temp': day4temp, 'day5temp': day5temp, 'day1desc': day1desc, 'day2desc': day2desc, 'day3desc': day3desc, 'day4desc': day4desc, 'day5desc': day5desc, 'day1icon': day1icon,
     'day2icon': day2icon, 'day3icon': day3icon, 'day4icon': day4icon, 'day5icon': day5icon, 'day1date': day1date, 'day2date': day2date, 'day3date': day3date, 'day4date': day4date, 'day5date': day5date})

