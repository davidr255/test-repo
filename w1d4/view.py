
import os
import time

def main_menu():
	os.system('cowsay -d "Welcome to my CLI app. -$(whoami)"')
	time.sleep(0)
	os.system('clear')
	print('\n[l] Look up\n[q] Quote\n[e] Exit')
	return input('\n what you wanna do?')

def lookup_menu():
	return input('Company Name: ')

def quote_menu():
	return input ('Ticker Symbol: ')

if __name__ == '__main__':
	main_menu()
