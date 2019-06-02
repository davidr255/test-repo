



def main_menu():
	print("\nWelcome to Terminal Teller!:\n\n    1) create account\n    2) log in\n    3) quit\n")
	return input ('Your choice: ')

def account_create_menu():
	print('\nAccount creation')
	fname = input('\nFirst Name : ')
	lname = input('Last Name  : ')
	pin_try = input('PIN: ')
	pin_confirm = input('confirm PIN: ')
	return fname,lname,pin_try,pin_confirm

def login_menu():
	account_num = input('Account number: ')
	pin_login = input('PIN: ')
	return account_num, pin_login

def account_menu(fname,lname,account_num):
	print("\nHello, {} {} ({})".format(fname,lname,account_num))
	print("\n    1) Check balance\n    2) Withdraw funds\n    3) Deposit funds\n    4) Sign out\n")
	return input ('Your choice: ')
	




