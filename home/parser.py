import json
import requests


class Weather:
    API_URL='http://api.openweathermap.org/data/2.5/find'

    @staticmethod
    def get_weather(location):
        pars = {'q': location, 'mode': 'json', 'units': 'metric'}
        result=  requests.post(Weather.API_URL,params=pars)
        datajs = json.loads(result.content)['list'][0]
        mainjs = datajs['main']
        fomatedjs = { 'city': datajs['name'], 'temp': mainjs['temp'],'pressure': mainjs['pressure'],'humidity': mainjs['humidity'] }
        return fomatedjs

