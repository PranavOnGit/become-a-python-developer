
#Example file for working with timedelta class

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#Construct a basic timedelta and print it.
print(timedelta(days=365, hours=5, minutes=1))

#Print todays date.
now = datetime.now()
print('Todays is: ', str(now))

#print todays date one year form now.
print('Date year from now is: ', str(now + timedelta(days=365)))

#create a timedelta that uses more then one argument.
print('In 2 days and 3 weeks it will be: ', str(now + timedelta(days=2, weeks=3)))

#calculate date 1 week ago, formated as a stirng.
tm = datetime.now() - timedelta(weeks=1)
str = tm.strftime('%A %B %d, %Y')
print('One week ago it was : '+ str)

#how many days until april fools days?
today = date.today()
afd = date(today.year, 4, 1)

#use date comparision to check april fool days has already gone for this year.
#if it has, use the use replace() to get the date of the year.
if afd < today:
    print("AFD already went by %d days ago" %((today - afd).days))
    afd = afd.replace(year = today.year+1)

#Now calculate amount of time until April Fools day 
time_to_afd = afd - today
print("It's just", time_to_afd.days, "Day's until AFD")
