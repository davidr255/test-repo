import json

import requests

class API:
	def __init__(self):
		self.endpoint = 'http://dev.markitondemand.com/ModApis/Api/v2'
	
	def lookup(self,company_name):
		self.endpoint += '/Lookup/json?input='+ company_name
		response = requests.get(self.endpoint).text
		return json.loads(response)[0]['Symbol']

	def quote(self,ticker_symbol):
		self.endpoint += '/Quote/json?symbol=' + ticker_symbol
		response = requests.get(self.endpoint).text
		return json.loads(response)['LastPrice']

if __name__ == '__main__':
	api = API()
	print(API().lookup('ford'))
	print(API().quote('f'))

