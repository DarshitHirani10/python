# Exercise 9: Calculate the date 4 months from the current date
from datetime import datetime,timedelta
given_date = datetime(2020, 2, 25).date()
print(datetime(given_date.year,given_date.month+4,given_date.day))
# print(given_date+timedelta(days=121))