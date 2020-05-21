import re
week = {'Monday': [],
	'Tuesday': [],
	'Wednesday': [],
	'Thursday': [],
	'Friday':[],
	'Saturday': [],
	'Sunday': [],}

valid_form = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')

def is_valid_format(n):

    return bool(valid_form.match(n))

def dict_str():

	for key, value in week.items():

		print(key, ', '.join(value))
	return print('-----------------\n')
def add_app():

	y = input('Enter day \n').title()

	if y in week:
		st = input('Enter start and start time in the following format HH:MM\n')
		en = input('Enter start and End time in the following format HH:MM\n')
		if is_valid_format(st) ==True and is_valid_format(en) == True:

			st_en = [st, en]

			return week[y].append("-".join(st_en))
		else:
			print('these are wrong format')
			add_app()
	else:
		print('thats wrong enter again')
		add_app()
def rem():

	day = input('What day do you want to remove from \n').title()
	if day in week:
		if week[day]:

			ti = input('Enter the time you want to remove in the following for HH:MM-HH:MM \n')
			if ti in  week[day]:

				week[day].remove(ti)
				return print('You have removed the following appointment %s' %ti)
			else:
				print('Thats invalid time')
				rem()
		else:
			print('No appointments for that day')
			return
	else:
		print('That day doesnt exist')
		rem()

x = input('Please use the following functions. \n ----------------- \nadd\nremove\nprint\nhelp\nday\nend\n')
while x != 'end':
	if x == 'add':
		add_app()
		print('You have added a new appointment')
	elif x == 'remove':
		rem()
	elif x == 'print':
		print('---Here is your week---\n')
		dict_str()
	elif x == 'day':

		n = input('Please enter the day you would like to see\n').title()
		if n not in week:
			print('That day does not exist please try again')
		else:
			print('Here are the appointments you have for %s' % n, week[n])
	elif x == 'help':
		print('----------------- \nadd\nremove\nprint\nhelp\nday\nend\n')
	else:
		print('Please use the following functions. \n ----------------- \nadd\nremove\nprint\nhelp\nday\nend\n')


	x = input()
