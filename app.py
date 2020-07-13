#here we create our flask application and call our API
#to call our API we need the link URL
import requests
import configparser

def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, api_key ):
    api_url= 'http://api.openweathermap.org/data/2.5/weather?zip={},&appid={}'.format(zip_code, api_key)
    r= requests.get(api_url)
    return r.json()
    #python will go ahead and request the data from the api url then
    #return it in json


print(get_weather_results("95129", get_api_key()))

