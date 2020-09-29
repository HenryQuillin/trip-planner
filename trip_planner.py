'''
Henry Quillin
9/24/2020
Python Trip Planner
'''
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
'''
'''
# If time difference + 12 is <= 24
midnight = 0
noon = 12
time_difference = int(input('What is the time difference, in hours, between your home and your destination? '))
adjusted_midnight = time_difference + midnight
adjusted_noon = time_difference + noon
midnight_msg = f'That means that when it is midnight at home it will be {adjusted_midnight} in your travel destination'
noon_msg = f'and when it is noon at home it will be {adjusted_noon}'
#if(time_difference <= 12 and time_difference >= 0):

if(time_difference < 0):
    adjusted_midnight = 24+time_difference


print(midnight_msg)
print(noon_msg)
'''
time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbole in front of the amount of hours. "))
    #our_time_input = 12
noon = 12
 # so the time difference could be + or -
 # convert the string to a int
int_time_difference = int(time_difference)
 # calculate from noon
difference_hrs = noon + int_time_difference
# these two condisions are on different days
if difference_hrs > 24:
    print("\n")
 # use % to get how many hours over into the next day
 # so if difference_hrs = 25
    next_day_differene = difference_hrs%24
    print(f'you are {next_day_differene} on the next day')# print you and 1hr(s) on the next day
if difference_hrs > 0:
    print("\n")
 # this is a negative number representing the previous day
 # so if difference_hrs = -2
 # -2%24
 # print you are  2hr(s) on the previous day
if difference_hrs >=24 and difference_hrs <=0:
    print("\n")
 # print difference_hrs



