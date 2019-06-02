import controller

from collections import defaultdict
import json


#data = {'100003':{'Last name': 'testlast','First name':'testfirst','Pin':'1234','Balance':0}}
#with open('account.json','w') as f:
#	json.dump(data,f)


def create_account(fname,lname,pin):
	with open('account.json') as json_file:
		data = json.loads(json_file.read())
		new_acct_num = int(sorted(data.keys())[-1]) + 1
		account_info = {'Last name':lname,'First name':
				fname,'Pin':pin,'Balance':0}
		data.update({new_acct_num:account_info})
	with open('account.json','w') as write_f:	
		json.dump(data,write_f)
	return new_acct_num
	
def login(account_num,pin_login):
	with open('account.json') as json_file:
		data = json.loads(json_file.read())
		if account_num in data:
			correct_pin = data[str(account_num)]['Pin']
			if pin_login == correct_pin:
				fname = data[account_num]['First name']
				lname = data[account_num]['Last name']
				return fname, lname
			else:
				print("Invalid pin. Try again\n.")
				controller.login_loop()
		else:
			print("Account not found. Please re-enter account number.")
			controller.login_loop()

def balance(input,fname,lname,account_num,deposit=0,withdraw=0):
	with open('account.json') as json_file:
		data = json.loads(json_file.read())
		old_bal = data[account_num]['Balance']
	if input == 'check':
		return old_bal
	elif input == 'update':
		if float(withdraw) > float(old_bal):
			print("!! INSUFFICIENT FUNDS !!")
			controller.account_loop(fname,lname,account_num)
		new_bal = float(float(old_bal) + float(deposit) - float(withdraw))
		data[account_num]['Balance'] = new_bal
		with open('account.json','w') as f:
			json.dump(data,f)
		return new_bal 			

