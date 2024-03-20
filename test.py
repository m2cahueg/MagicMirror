#! python3

import datetime
from dateutil.relativedelta import relativedelta
import requests
import bs4

#Declaring Variables

owner = 'Greg'
birth_date = datetime.datetime.strptime('8/16/1987', '%m/%d/%Y')
birthday_countdown = 0
time = datetime.datetime.now()
age = 0
part_of_day = ''
printed_time = time.strftime("%I:%M %p")
printed_day = time.strftime("%A, %B %d of %Y")

#Determining the Part of Day 
if time.hour < 6:
	part_of_day = 'Night'
elif time.hour < 12:
	part_of_day = 'Morning'
elif time.hour < 18:
	part_of_day = 'Afternoon'	
else:
	part_of_day = 'Evening'
	
#Determining the owner's age and next_age

if time.month < birth_date.month:
	age = time.year - birth_date.year - 1 
elif time.month < birth_date.month:
	age = time.year - birth_date.year
elif time.day < birth_date.day:
	age = time.year - birth_date.year - 1
else:
	age = time.year - birth_date.year

next_age = age + 1
next_birthday = birth_date + relativedelta(years=next_age)

#Determining the number of days until the owners next birthday.

birthday_countdown = next_birthday - time
retirement_countdown = birth_date + relativedelta(years=67) - time

#Parsing Data

greeting = f"Good {part_of_day}, {owner}!" 
time_statement = f"It is {printed_time} on {printed_day}.\n"
birthday_statement = f"There are {birthday_countdown.days} days until you turn {next_age} years old.\n"
retirement_statement = f"There are {retirement_countdown.days} days until you retire.\n"
greeting_html = f"<P> <h1> {greeting} </h1>"
time_statement_html = f"<P> {time_statement}"
birthday_statement_html = f"<P> {birthday_statement}"
retirement_statement_html = f"<P> {retirement_statement}"

#Outputing Data 

print(greeting)
print(time_statement)
print(birthday_statement)
print(retirement_statement)
print(next_birthday) 

file = open('/var/www/html/index.html','w')
file.write('<HTML>\n')
file.write('<body style="background-color:black;">\n')
file.write('<body text="#ffffff" link="#ff0000" vlink="#ff0000" alink="#ff0000">\n')
file.write('<HEAD>\n')
file.write('<style>\n')
file.write('h1 {text-align: center;}\n')
file.write('p {text-align: left;}\n')
file.write('div {text-align: center;}\n')
file.write('</style>\n')
file.write(greeting_html)
file.write('</HEAD>\n')
file.write(time_statement_html)
file.write(birthday_statement_html)
file.write(retirement_statement_html)
file.write('</BODY>\n')
file.write('</HTML>\n')
file.close() 
 
