# import statements

import unittest
import requests
import activity6


class Current_Conditions_activity(unittest.TestCase):
	api_start = 'https://api.openweathermap.org/data/2.5/weather?q='

	api_key = '&appid=YOUR API KEY HERE !!!'

	city = 'xyz'

	country = 'xyz'

	url = api_start + city + ',' + country + api_key

	json_data = requests.get(url).json()

	def test_conditions_for_exceptions(self):
		result = activity6.check_current_conditions(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_current_temperature_for_exceptions(self):
		result = activity6.current_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_current_humidity_for_exceptions(self):
		result = activity6.current_humidity(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_low_temperature_for_exceptions(self):
		result = activity6.low_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_high_temperature_for_exceptions(self):
		result = activity6.high_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)


if __name__ == '__main__':
	unittest.main()
