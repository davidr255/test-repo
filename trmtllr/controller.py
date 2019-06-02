import sys
import model
import view

def main_loop():
	user_input = view.main_menu()
	account_input = '1'
	login_input = '2'
	quit = '3'
	if user_input == account_input:
		account_create_loop()
	if user_input == login_input:
		login_loop()
	if user_input == quit:
		print("Goodbye.")
		exit()
		
def account_create_loop():
	fname,lname,pin_try,pin_confirm = view.account_create_menu()
	if pin_confirm == pin_try:
		pin = pin_try
		new_account_num = model.create_account(fname,lname,pin)
		print("account created, your account number is {}.".format(new_account_num))
		main_loop()
	else:
		print("Please confirm pin matches and re-enter")
		account_create_loop()

def login_loop():
	account_num, pin_login = view.login_menu()
	fname, lname = model.login(account_num,pin_login)
	account_loop(fname,lname,account_num)

def account_loop(fname,lname,account_num):
	user_input = view.account_menu(fname,lname,account_num)
	if user_input == '1':
		user_balance = model.balance('check',fname,lname,account_num)
		print("Your balance is ${r:1.2f}".format(r=user_balance))
	elif user_input == '2':
		withdraw = float(input("\nHow much to withdraw: "))
		new_bal = model.balance('update',fname,lname,account_num,0,withdraw)
		print("Your new balance is ${r:1.2f}".format(r=new_bal))		
	elif user_input == '3':
		deposit = float(input("\nHow much to deposit:  "))
		new_bal = model.balance('update',fname,lname,account_num,deposit)
		print("Your new balance is ${r:1.2f}".format(r=new_bal))	
	elif user_input == '4':
		print("Back to main menu.")
		main_loop()
	account_loop(fname,lname,account_num)


if __name__ == '__main__':
	main_loop()

