import json
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv('./.env')
import requests

def index(request):
    return render (request , "main.html")
    
def home(request):
    context = {
        'api_key' : os.environ.get("maps_api"),
        'origin' : 'Lucknow + Uttar Pradesh',
        'destination': 'Kanpur + Uttar Pradesh',
    }
    return render (request , "home.html" , context)

def directions(request):
    context = {
        'api_key' : os.environ.get("maps_api"),
        'origin' : 'Lucknow + Uttar Pradesh',
        'destination': 'Kanpur + Uttar Pradesh'
    }
    return render(request , 'first.html' , context)

def location(request):
    res = {}
    if request.method == "POST":
        body = json.loads(request.body)
        lat = body['lat']
        long = body['long']
        URL = "https://api.opencagedata.com/geocode/v1/json?q="+ lat + "+" + long + "&key="+os.environ.get("open_api")
        r = requests.get(url = URL)
        data = r.json()
        res['data'] = data['results'][0]['components']
        res['data'].pop("ISO_3166-1_alpha-2" , True)            
        res['data'].pop("ISO_3166-1_alpha-3", True)
        res['data'].pop("_category", True)
        res['data'].pop("_type", True)
        res['data'].pop("country_code", True)
        res['data'].pop("place_of_worship", True)
        res['data'].pop("state_code", True)
        res['data'].pop("suburb", True)
        res['data'].pop("continent", True)
        res['data'].pop("country", True)
        res['data'].pop("country_code" , True)
        res['data'].pop("postcode", True)
        res['data'].pop("district", True)
        res['data']['address'] = ""
        for i in res['data'].items():
            if(i[0]!='address'):
                res['data']['address']+=i[1] + ","
        res['data']['address']=res['data']['address'][:-1]
        return JsonResponse(res , safe=False , status =200)

    res['msg'] = "Mathod not allowed"
    return JsonResponse(res , safe= False , status = 405)

def main(request , pick , drop):
    res = {}
    if request.method == 'GET':
        context = {
            'api_key' : os.environ.get("maps_api"),
            'origin' :  pick,
            'destination': drop,
        }
        return render (request , "weather.html" , context)
    res['msg'] = "method not allowed"
    return JsonResponse(res , safe = False , status = 405)

def get_coordinates(request):
    res = {}
    if request.method == "POST":
        data = json.loads(request.body)
        drop = data['drop']
        print(drop)
        URL = "https://api.opencagedata.com/geocode/v1/json?q="+drop+ "&key="+os.environ.get("open_api")
        r = requests.get(url = URL)
        result = r.json()
        res['data'] = {
            "lat" : result['results'][0]['bounds']['northeast']['lat'],
            "long":result['results'][0]['bounds']['northeast']['lng']
        }
        res['msg'] = "success"
        return JsonResponse(res , safe=False , status =200)
    res['msg'] = "method not allowed"
    return JsonResponse(res , safe=False , status =405)

def get_weather(request):
    res = {}
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        lat = data['lat']
        lon = data['long']
        url = "http://api.weatherbit.io/v2.0/current"
        params = {"key" : os.environ.get("weather_api") , "lat" : lat , "lon" :lon}
        r = requests.request("GET", url, params=params)
        response = r.json()
        res['data'] = {
            "icon" : "https://www.weatherbit.io/static/img/icons/" +response['data'][0]['weather']['icon'] + ".png",
            "weather_desc" :response['data'][0]['weather']['description'],
            "temp_in_celcius" : response['data'][0]['temp']
        }
        return JsonResponse(res , safe=False , status =200)
    res['msg'] = "method not allowed"
    return JsonResponse(res , safe=False , status =405)


