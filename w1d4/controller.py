
import model
import view

def game_loop():
	user_input = view.main_menu()
	lookup_inputs = ['l','lookup','look-up','lookup']
	quote_inputs = ['q','quote']
	acceptable_inputs = lookup_inputs \
			    +quote_inputs
	if user_input in acceptable_inputs:
		if user_input in lookup_inputs:
			x = view.lookup_menu()
			y = model.lookup(x)
			print(y)
		elif user_input in quote_inputs:
			x = view.quote_menu()
			y = model.quote(x)
			print(y)
		else:
			print('Error: uncaught exception')
	else:
		print('Error: uncaught exception')

if __name__ == '__main__':
	game_loop()
