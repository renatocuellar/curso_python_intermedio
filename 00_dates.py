# Dates

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.year)
    print(date.month)
    print(date.timestamp)

print_date(now)

year_2024 = datetime(2024, 11, 13)

print_date(year_2024)

from datetime import time

current_time = time(21, 6, 15)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2023, 11, 13)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2024 - now
print(diff)

from datetime import timedelta

init_timedelta = timedelta(200, 100, 200, weeks = 10)
end_timedelta = timedelta(300, 200, 50, weeks = 15)
print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)