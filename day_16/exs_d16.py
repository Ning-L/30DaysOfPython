# Day 16: 30 Days of python programming

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
current = datetime.now()

print("Current day is :", current.day)
print("Current month is :", current.month)
print("Current year is :", current.year)
print("Current hour is :", current.hour)
print("Current minute is :", current.minute)
print("Current timestamp is :", current.timestamp())


# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current.strftime("%m/%d/%Y, %H:%M:%S") # '07/16/2024, 15:35:07'


# 3. Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
today_date = datetime.strptime(today, "%d %B, %Y") # need to match date string in same order, otherwise ValueError


# 4. Calculate the time difference between now and new year.
new_year = datetime.today()

time_diff = new_year - today_date
print("Time difference is", time_diff)


# 5. Calculate the time difference between 1 January 1970 and now.
old_time = datetime.strptime("1 January 1970", "%d %B %Y")
now = datetime.today()
print("Time difference is", now - old_time)


# 6. Think, what can you use the datetime module for? Examples:
    ## - Time series analysis
    ## - To get a timestamp of any activities in an application
    ## - Adding posts on a blog
"""
- obtain execution time of some codes
- check if file was modified by comparing with a speficy timestamp
"""