year = input('Please input a year: ')
year = int(year)

def is_leap(year): #is it a leap year
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

print(is_leap(year))