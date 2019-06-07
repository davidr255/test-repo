#!/usr/bin/env python3

import json

import requests

# from mappers import Database


class Schema:

#	def __init__(self,username,password):
#		self.username = username
#		self.password = password

	def lookup_api():
		endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/lookup/json?input='
		return endpoint

	def lookup(self,company):
		api = Schema.lookup_api()
		query = api + company
		# print(query)
		return json.loads(requests.get(query).text)[0]['Symbol']

	def quote(self,symbol):
		api = Schema.quote_api()
		query = api + symbol
		return json.loads(requests.get(query).text)['LastPrice']

	def quote_api():
		endpoint= 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='
		return endpoint


if __name__ == '__main__':
	company = input('Company Name : ')
	symbol = Schema().lookup(company)
	print(symbol)
	print(Schema().quote(symbol))
