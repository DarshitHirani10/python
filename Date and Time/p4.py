# Exercise 4: Print a date in a the following format
# Day_name  Day_number  Month_name  Year
from datetime import datetime,timedelta
given_date = datetime(2025, 4, 22)
print(given_date.strftime('%A %d %B %Y'))