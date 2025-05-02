# Solution 1 - using datetime Module

from datetime import datetime

date = "Oct 14 1997 7:15AM"
print(type(date))

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")

print(date_time)
print(type(date_time))

# Solution 2 - using dateutil Module
# pip3 install python-dateutil
# python.exe -m pip install --upgrade pip

from dateutil import parser

temp_date_time = parser.parse("Oct 14 1997 7:15AM")
print(temp_date_time)
print(type(temp_date_time))
