#here I create  flask application and call weather API
#to call the API I'd need the link URL
#use zip code : 95129 bc the country isn't defined.
import requests
import configparser
from flask import Flask, render_template, request

#first; initilize the flask app
app= Flask(__name__) #name is configured to be the name of the application during run time

#second; map the app using routs
#route for index page
@app.route('/')
def weather_dashboard():
    return render_template('home.html')

#route for result page
@app.route('/results', methods=['POST']) #the way to access this is via a POST Req
def render_results():
    zip_code= request.form['zipCode'] #Accessing the html element named zipCode
    api_key= get_api_key()
    data= get_weather_results(zip_code,api_key)
    temp= "{0:.2f}".format(data["main"]["temp"]) #to get a value from the dictionary as string
    feels_like= "{0:.2f}".format(data["main"]["feels_like"])
    weather= data["weather"][0]["main"] #array not a dictionary
    location= data["name"]
    return render_template('results.html', location=location,temp=temp,
                           feels_like=feels_like, weather=weather )

def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(zip_code, api_key ):
    api_url= 'http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}'.format(zip_code, api_key)
    r= requests.get(api_url)
    return r.json()
    #python will go ahead and request the data from the api url then
    #return it in json

#just to check
print(get_weather_results("95129", get_api_key()))

#should be the last line
if __name__== '__main__':
    app.run() #this ensures the app only run once and multiple instances are not crated
