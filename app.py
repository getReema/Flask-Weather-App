#here we create our flask application and call our API
#to call our API we need the link URL
import requests
import configparser
from flask import Flask, render_template, request

#first; initilize the flask app
app= Flask(__name__) #name is configured to be the name of the application during run time

#second; map the app using routs
@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST']) #the way to access this is via a POST Req
def render_results():
    zip_code= request.form['zipCode'] #Accessing the html element named zipCode
    return "Zip Code: "+ zip_code


if __name__== '__main__':
    app.run() #this ensures the app only run once and multiple instances are not crated


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

