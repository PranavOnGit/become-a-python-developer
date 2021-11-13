
#import modules
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS path
    print(os.name)

    # check for item existance and type
    print("This item exist: " + str(path.exists('textfile')))
    print("This item exist is File: " + str(path.isfile('textfile')))
    print("This item exist is Directory: " + str(path.isdir('textfile')))

    # Work with file paths
    print("Path of this Item :"+ str(path.realpath('textfile')))
    print("Path of this Item Seprately:"+ str(path.split(path.realpath('textfile'))))

    # Get the modification time
    tim = time.ctime(path.getmtime('textfile'))
    print(tim)
    tim = datetime.datetime.fromtimestamp(path.getmtime('textfile'))
    print(tim)
    
    # Calculate how long ago the item was modified 
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('textfile'))
    print('It has been '+ str(td)+' since file was modified')
    print('It has been '+ str(td.total_seconds()) +' Seconds since file was modified')


    
if __name__ == "__main__":
    main()