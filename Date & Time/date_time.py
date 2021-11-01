#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print('Today\'s Date is: ', today)
  
  # print out the date's individual components
  day = today.day
  month = today.month
  year = today.year
  print('Date is: ', day, month, year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print('Today\'s Weekday is: ', today.weekday())
  days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  print('Which days is a:', days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  todayDateTime = datetime.now()
  print('Current Date-Time is: ', todayDateTime)
  
  # Get the current time
  currentTime = datetime.time(datetime.now())
  print('Current Time is: ', currentTime)
  
if __name__ == "__main__":
  main();
  