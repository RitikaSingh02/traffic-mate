import json
from django.http.response import JsonResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv('./.env')
import requests

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
        URL = "https://api.opencagedata.com/geocode/v1/json?q="+ lat + "+" + long + "&key=2a8d82c976924560a9948c81e6d11d77"
        r = requests.get(url = URL)
        data = r.json()
        if("city" in data['results'][0]['components']):
            city =  data['results'][0]['components']['city']
        else:
            city = ""
        district = data['results'][0]['components']['state_district']
        state = data['results'][0]['components']['state']
        country = data['results'][0]['components']['country']
        county = data['results'][0]['components']['county']
        res['data'] = {
            "district" : district,
            "state" : state , 
            "city" : city,
            "country" : country,
            "county" : county
        }
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
        return render (request , "first.html" , context)
    res['msg'] = "method not allowed"
    return JsonResponse(res , safe = False , status = 405)