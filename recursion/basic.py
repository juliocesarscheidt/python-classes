from math import floor
from datetime import datetime

"""
it's going to calculate the age from the specified date
until the first day of that month, recursively
"""
def calculate_age_recursive(birth_date: datetime):
  print('-----------------------------------------------')
  print('birth_date', birth_date)

  datetime_now = datetime.now()

  print('datetime_now', datetime_now)

  years = floor((datetime_now - birth_date).days / 365)
  print('years', years)

  if birth_date.day > 1:
    previous_date = datetime(birth_date.year, birth_date.month, birth_date.day - 1, 0, 0, 0, 0)
    print('previous_date', previous_date)

    calculate_age_recursive(previous_date)

calculate_age_recursive(datetime(1996, 7, 8, 0, 0, 0, 0))
