#!/usr/bin/env python3

import json

import requests

from mappers import Database


class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        # SELECT password FROM users WHERE username='{submitted_username}';
        with Database() as d:
            d.cursor.execute(
                f'''SELECT password
                    FROM users
                    WHERE username='{self.username}';''')
            password = d.cursor.fetchone()[0]
            if password:
                if self.password == password:
                    return True
            return False

def lookup(company):
    api = lookup_api()
    company = company
    query = api + company
#    print(query)
    return json.loads(requests.get(query).text)[0]['Symbol']


def quote(symbol):
    symbol = symbol
    api = quote_api()
    query = api + symbol
#    print(query)
    return json.loads(requests.get(query).text)['LastPrice']

def lookup_api():
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/lookup/json?input='
    return endpoint

def quote_api():
    endpoint= 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='
    return endpoint


if __name__ == '__main__':
    #user = User('cookiemonster','opensesame')
    #print(user.login())
    company = input('company name: ')
    print(lookup(company))
#    symbol = input('stock symbol: ')
#    print(quote(symbol))
