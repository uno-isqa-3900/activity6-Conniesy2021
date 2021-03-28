#Date: 26/3/2021
#Class: ISQA3900
#Purpose:Learn to use API and JSON
#Name: Siyu Pan

from datetime import datetime
import requests
import pytemperature
now = datetime.now()

print("ISQA 3900 Open Weather API")
print(now.strftime('%A, %B %d, %Y'))
print()
choice = "y"
while choice.lower() == "y":
    try:
        city = input("Enter city: ")
        print("Use ISO letter country code like: https://countrycode.org/")
        country = input("Enter country code: ")
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_key = '&appid=bb5ca18932706e1b9c7ef4baec4c64f1'
        url = api_start + city + ',' + country + api_key
        json_data = requests.get(url).json()
        weather_description = json_data['weather'][0]['description']
        print("Current conditions: ", weather_description)
        weather_temperature = pytemperature.k2f(json_data['main']['temp'])
        print("Current Temperature in Fahrenheit: ", weather_temperature)
        current_pressure = json_data['main']['pressure']
        print("Current Pressure in hpa: ", current_pressure)
        current_hum = json_data['main']['humidity']
        print("Current Humidity: ", current_hum, end='')
        print("%")
        low_temp = pytemperature.k2f(json_data['main']['temp_min'])
        print("Expected Low Temperature in Fahrenheit: ", low_temp)
        high_temp = pytemperature.k2f(json_data['main']['temp_max'])
        print("Expected High Temperature in Fahrenheit: ", high_temp)

    except KeyError:
        print("     Unable to access {} in {}".format(city,country))
        print("     Verify city name and country code")

    finally:
        choice = input("Continue (y/n)?: ")
        print()

print('Bye')