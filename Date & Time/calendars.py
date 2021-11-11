
#import calender 
import calendar

#print text formated calnder 
c = calendar.TextCalendar(calendar.MONDAY)
tc = c.formatmonth(2021, 1, 0, 0)
print(tc)

#print HTML formated calnder
Hc = calendar.HTMLCalendar(calendar.SUNDAY)
hc = Hc.formatmonth(2021, 1, 1)
print(hc)

#loop over the days of a month
#zeros means that the day of the week is in an overloping month
cal = calendar.TextCalendar(calendar.MONDAY)
for i in cal.itermonthdays(2021, 8):
    print(i)

#the calendar module provides useful utilities for the given local, 
# such as name of days and months in both full and abrivated forms
for day in calendar.day_name:
    print(day)

for name in calendar.month_name:
    print(name)

#calculate days based on a rule: For example, consider: 
#a team meeting first friday of every month to figure out what days that would be for each month ,
#we can use this script: 
print("Team meeting will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] == 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))



