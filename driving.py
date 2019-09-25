nationality = input('PLS input your nationality, TW or USA? ')
if nationality == 'TW' or nationality == 'USA':
	age = input('PLS input your age: ')
	age = float(age)
	if nationality == 'TW':
		if age >= 18:
			print('you can get driving permit in TW')
		else:
			print('Sorry, you must be 18-yr old in TW to get driving permit')
	