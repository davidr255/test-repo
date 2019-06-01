import wrapper


def lookup(company_name):
	return wrapper.API().lookup(company_name)

def quote(ticker_symbol):
	return wrapper.API().quote(ticker_symbol)


if __name__ == '__main__':
	print(lookup('tesla'))
	print(quote('GM'))
