import datetime
now= datetime. datetime. now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
from datetime import date
d0= date(2009, 10, 30)
d1= date(2010, 12, 31)
delta= d1- d0
print (delta.days)
print("One year later the dates would be")
d0= date(d0.year+ 1, d0.month, d0.day)
d1= date(d1.year+ 1, d1.month, d1.day)
print(d0, d1)
