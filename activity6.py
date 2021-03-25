import urllib.parse
import requests
import pytemperature


def check_current_conditions(json_data):

    try:
        current_conditions = json_data['weather'][0]['description']
        return current_conditions

    except Exception:
        str = 'Please enter valid input'
        return str


def current_temperature(json_data):
    pass
    
def current_humidity(json_data):
    pass
    
def low_temperature(json_data):
    pass
   
def high_temperature(json_data):
    pass
   
if __name__ == '__main__':

    choice = 'y'
    while choice.lower() == 'y':
        print("ISQA 4900 Open Weather API")
        city = input('Enter city: \t')
        print('Use ISO letter country code like: https://countrycode.org/')
        country = input('Enter the country code: \t')
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_key = '&appid=YOUR API KEY HERE !!!'
        url = api_start + city + ',' + country + api_key
        json_data = requests.get(url).json()
        current_conditions = check_current_conditions(json_data)
        print('Current conditions: '+ current_conditions)
        choice = input("Continue(y/n)?")
        print()
        print("Bye!")