from datetime import datetime, date, timedelta
from time import time

# datetime.now() returns the current date and time with timezone
datetime_now = datetime.now()
# datetime_now = datetime.utcnow()
datetime_now = datetime(2022, 1, 25, 14, 4, 48, 919115)
print('datetime_now', datetime_now)
# datetime_now 2022-01-25 14:04:48.919115

print('type(datetime_now', type(datetime_now))
# type(datetime_now <class 'datetime.datetime'>

# format
print('strftime', datetime_now.strftime('%Y-%m-%dT%H:%M:%S.000+00:00'))
# strftime 2022-01-25T14:04:48.000+00:00

print('strftime', datetime_now.strftime("%Y%m%d%H%M%S"))
# strftime 20220125140448

# ISO 8601
print('isoformat', datetime_now.isoformat())
# isoformat 2022-01-25T14:04:48.919115

# unix timestamp seconds https://www.unixtimestamp.com/
print('timestamp', datetime_now.timestamp())
# timestamp 1643130288.919115

print('year', datetime_now.year)
# 2022
print('month', datetime_now.month)
# 1
print('day', datetime_now.day)
# 25

datetime_yesterday = (datetime_now - timedelta(days=1))
print('datetime_yesterday', datetime_yesterday)
# datetime_yesterday 2022-01-24 14:04:48.919115

print()

print('today', date.today())
# 2024-02-04

# convert from string to datetime object
print('strptime', datetime.strptime('2022-01-25', '%Y-%m-%d').isoformat())
# strptime 2022-01-25T00:00:00

print()

# time() returns the current time in seconds
def current_milli_time():
  return round(time() * 1000)

print('current_milli_time', current_milli_time())
# current_milli_time 1707080691303

print()

def current_milli_from_time(__time):
  return round(__time * 1000)

print('datetime_yesterday.timestamp ms', current_milli_from_time(datetime_yesterday.timestamp()))
# datetime_yesterday.timestamp ms 1643043888919
print('datetime_now.timestamp ms', current_milli_from_time(datetime_now.timestamp()))
# datetime_now.timestamp ms 1643130288919

print()

# time() returns the current time in seconds
time_now = time()
time_now = 1643129999.1912985
print('time_now', time_now)
# time_now 1643129999.1912985

print('date.fromtimestamp', date.fromtimestamp(time_now))
# date.fromtimestamp 2022-01-25

datetime_fromtimestamp_iso = datetime.fromtimestamp(time_now).isoformat()
print('datetime.fromtimestamp iso', datetime_fromtimestamp_iso)
# datetime.fromtimestamp iso 2022-01-25T13:59:59.191298

# print('datetime.fromisoformat', datetime.fromisoformat('2022-01-25T13:59:59.191298'))
print('datetime.fromisoformat', datetime.fromisoformat(datetime_fromtimestamp_iso))
# datetime.fromisoformat 2022-01-25 13:59:59.191298
