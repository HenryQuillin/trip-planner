'''
Henry Quillin
9/24/2020
Python Trip Planner
'''

# Part 1 – Greeting
print('Welcome to Vacation Planner!')
cust_name = input('Whats your Name? ')
destination = input('Nice to meet you ' + cust_name + ', where are you traveling to? ')
print('Great! ' + destination + ' sounds like a great trip')
print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø')
print(' ')
num_of_days = int(input('How many days are you going to spend traveling? '))
budget = int(input('How much money are you going to spend on this trip? '))
currency = input('What is the three letter currency symbol for your travel destination?')
conversion_rate = float(input('How many MXC are there in 1 USD?'))
print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø')
print(' ')

# Part 2 - Travel time and budget
hours = num_of_days * 24
minutes = hours * 60
print(f'If you are traveling for {num_of_days} days that is the same as {hours} hours or {minutes} minutes')

daily_budget = budget/num_of_days
print(f'If you are going to spend {budget} {currency} that means per day you can spend up to {daily_budget} {currency}')
print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø')
print(' ')

#Part 3 - Time Difference Converter
time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbole in front of the amount of hours: "))
    #our_time_input = 12
noon = 12
destination = 'mexico'
midnight = 0
 # so the time difference could be + or -
 # convert the string to a int
int_time_difference = int(time_difference)
 # calculate from noon
difference_hrs_noon = noon + int_time_difference
difference_hrs_midnight = midnight + int_time_difference
# use % to get how many hours over into the next day could be + or -
adjusted_noon = difference_hrs_noon%24
adjusted_midnight = difference_hrs_midnight%24

if difference_hrs_noon <= 24 and difference_hrs_noon >0:
    print(f'When it is noon at home it will be {adjusted_noon}:00 on the same day in {destination}')
elif difference_hrs_noon > 24:
    print(f'When it is noon at home it will be {adjusted_noon}:00 on the next day in {destination}')
else:
    print(f'When it is noon at home it will be {adjusted_noon}:00 on the previous day in {destination}')

if difference_hrs_midnight <= 24 and difference_hrs_midnight >0:
    print(f'When it is midnight at home it will be {adjusted_midnight}:00 on the same day in {destination}')
elif difference_hrs_midnight > 24:
    print(f'When it is midnight at home it will be {adjusted_midnight}:00 on the next day in {destination}')
else:
    print(f'When it is midnight at home it will be {adjusted_midnight}:00 on the previous day in {destination}')



print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø')
print(' ')

#Part 4 - km^2 to miles^2
km = int(input('What is the square area of your destination country in km^2? '))
print(f'In miles^2 that is {km/2.59}')


