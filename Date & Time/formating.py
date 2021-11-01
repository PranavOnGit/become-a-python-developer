

from datetime import datetime

def main():
    #date and time can be formated using a set of predefiend string 
    #control codes
    now = datetime.now()

    ##### Date Formatting #####

    # %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, $d - Day of month
    print(now.strftime("Year is : %y"))
    print(now.strftime("%a, %d, %B, %y"))

    # %c - locale's date and time, %x - locals date, %X- local's time
    print(now.strftime("Local date-time is: %c"))
    print(now.strftime("Local date is: %x"))
    print(now.strftime("Local time is: %X"))


    ##### Time Formatting #####
  
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time is: %I:%M:%S %p "))
    print(now.strftime("Current time is: %H:%M:%S %p "))

if __name__ == "__main__":
    main()