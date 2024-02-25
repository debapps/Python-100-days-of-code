import datetime

# Constants
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Current Date and Time.
now = datetime.datetime.now()
print(type(now))
print(f'Current Date Time: {now}')

year = now.year
month = now.month
date = now.day
day_of_week = now.weekday()

print(f'Year: {year}\nMonth: {month}\nDate: {date}')
print(f'Day of week: {WEEKDAYS[day_of_week]}')

# Creating datetime object.
birth_day = datetime.datetime(year=1987, month=8, day=14, hour=13, minute=18)
print(f'My Birth Day: {birth_day}')