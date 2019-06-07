
from models import User
import time

def infinite_loop():
	username = input('Your application username: ')
	password = input('Your application password: ')
	stored_un = user.fetch_username()
	stored_pw = user.fetch_password()
	if username == stored_un:
		if password = stored_pw:
			return 'successful login'
	return 'catch-all'

if __name__ == '__main__':
	print(infinite_loop())
