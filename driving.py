nationality = input('PLS input your nationality, TW or USA? ')
while True:
	if nationality == 'TW' or nationality == 'USA':
		age = input('PLS input your age: ')
		age = float(age)
		if nationality == 'TW':
			if age >= 18:
				print('you can get driving permit in TW')
			else:
				print('Sorry, you must be 18-yr old in TW to get driving permit')
		else:
			if age >= 16:
				print('you can get driving permit in USA')
			else:
				print('Sorry, you must be 16-yr old in TW to get driving permit')
		break
	else:
		print('you are neither TW nor USA citizen')
		print('PLS re-input nationality, TW or USA! or Q to quit')
		nationality = input('PLS input your nationality, TW or USA? ')
		if nationality == 'Q':
			break
