# Dates a very important because these are used in almost every type of applications.
# In python we have dates, times, date-times, time zones, time deltas etc.
# We can work with that by importing datetime module.

import datetime
# We can work with two types of datetime -> 1. naive datetimes 2. aware datetimes.
# Naive datetimes don't have enough information to determine things like time zones or daylight savings times,
# But naive datetimes are easier to work with if we don't need that level of detail,
# But if we need that level of detail to avoid confusion then we need to use aware datetimes,
# As they contain informations about time zones and daylight saving times.

'''We will first start with naive datetimes.'''

# There are different ways to create a date like ->
# datetime.date is used to work with dates -> year, month and day

# variable = datetime.date(y,m,d) used to create a specific date.
d = datetime.date(2016, 7, 24)
print(d) # Output -> 2016-07-24
# Note: Don't write leading zeros like datetime.date(2016, 07, 24) 
# Python 3 raises a SyntaxError for number literals starting with 0.
# Just write 7, not 07 — Python displays it as "07" in the output automatically, that's just formatting. 

# variable = datetime.date.today() will give today's date.
tday = datetime.date.today()
print(tday) # Output -> 2026-08-29

# prints current year.
tday = datetime.date.today()
print(tday.year) # Output -> 2026
# prints current month.
tday = datetime.date.today()
print(tday.month) # Output -> 8
# prints current day.
tday = datetime.date.today()
print(tday.day) # Output -> 29

# We can also get day of the week -> 

# For weekday() -> Monday => 0 | Sunday => 6
tday = datetime.date.today() 
print(tday.weekday()) # Output -> 5
# For isoweekday() -> Monday => 1 | Sunday => 7
tday = datetime.date.today()
print(tday.isoweekday()) # Output -> 6 

# Now let's take a look at time Deltas.
# Time Deltas are difference between two dates or times.
# This are useful when we want to do operations on dates or times.

tday = datetime.date.today() # Will store today's date in tday variable.
tdelta = datetime.timedelta(days=7) # can combine days with hours, minutes, seconds, weeks, milliseconds, or microseconds.
# but we can not use months or years as time-deltas, as their lengths fluctuate due to leap years and varying month lengths.
# tdelta = datetime.timedelta(days=7) creates an object that represents a time duration of exactly 7 days.
# It is primarily use it to calculate future or past dates, it acts like a countdown or an offset.
# It does not represent a specific date on the calendar,
# but rather a relative span of time (a time "difference" or "delta") that we can add to or subtract from other dates. 
print(tday + tdelta) # Output -> 2026-09-05  

tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday - tdelta) # Output -> 2026-08-22 

# If we add or substract a date1 with time_delta then we will get result as date2.
# If we add or substract date1 and date2 then we will get a time_delta as a result.
# date2 = date1 + timedelta
# timedelta = date1 + date2
tday = datetime.date.today()
bday = datetime.date(2026, 10, 25)
till_bday = bday - tday 
print(till_bday) # Output -> 57 days, 0:00:00
print(till_bday.days) # Output -> 57 days 
print(till_bday.total_seconds()) # Output -> 4924800.0

# datetime.time is used to work with time -> hour, minutes, seconds and micro seconds.

# variable = datetime.time(hour, minutes, seconds, micro_seconds)
t = datetime.time(9, 30, 45, 100000)
print(t) # Output -> 09:30:45.100000

t = datetime.time(9, 30, 45, 100000)
print(t.hour) # Output -> 9

t = datetime.time(9, 30, 45, 100000)
print(t.minute) # Output -> 30

t = datetime.time(9, 30, 45, 100000)
print(t.second) # Output -> 45

t = datetime.time(9, 30, 45, 100000)
print(t.microsecond) # Output -> 100000 

# To access both date and time we can use ->

# variable = datetime.datetime(year, month, day, hour, minute, seconds, microseconds)
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt) # Output -> 2016-07-26 12:30:45.100000

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.date()) # Output -> 2016-07-26

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.time()) # Output -> 12:30:45.100000

# can also do this with month, day, hour, minute, second, microsecond.
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.year) # Output -> 2016

# We can also use timedelta here ->
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta = datetime.timedelta(days=7)
print(dt + tdelta) # Output -> 2016-08-02 12:30:45.100000

# Can do timedelta with -> weeks: float = 0
#                          days: float = 0
#                          hours: float = 0
#                          minutes: float = 0
#                          seconds: float = 0,
#                          microseconds: float = 0,
#                          milliseconds: float = 0,
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta = datetime.timedelta(hours=7)
print(dt + tdelta) # Output -> 2016-07-26 19:30:45.100000

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta = datetime.timedelta(weeks=2)
print(dt + tdelta) # Output -> 2016-08-09 12:30:45.100000

# datetime.datetime() with current date and time can be accessed by ->

dt_today = datetime.datetime.today()
print(dt_today) #Output -> 2026-08-29 22:36:23.809280
# datetime.datetime.today() not give option for timezone 
# but we can pass timezone in datetime.datetime.now(timezone)
dt_now = datetime.datetime.now()
print(dt_now) # Output -> 2026-08-29 22:36:23.809532

# datetime.datetime.utcnow() is older version and will be removed in future python versions.
# So for python version 3.11 or newer use dt_utcnow = datetime.datetime.now(datetime.UTC)
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow) # Output -> 2026-08-29 17:06:23.886452
# DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version.

dt_utcnow = datetime.datetime.now(datetime.UTC)
print(dt_utcnow) # Output -> 2026-08-29 17:06:23.886522+00:00

# datetime.datetime.utcnow() gives UTC time but is NAIVE (no tzinfo) — that's why it's being deprecated.
# datetime.datetime.now(datetime.UTC) gives UTC time AND is timezone-AWARE (notice the +00:00 in the output).
# So for UTC time with proper timezone info, prefer datetime.datetime.now(datetime.UTC) going forward.

'''Interacting with TimeZones using pytz'''
'''Working with aware time zones'''

import pytz

# creating timezone aware datetime using utc
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt) # Output -> 2016-07-27 12:30:45+00:00
# +00:00 is UTC offset.

# Now let's get UTC Time which is also timezone aware.
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow) # Output -> 2026-08-29 18:19:22.769406+00:00
# This is the current utc time.

# Lets see how to convert utc aware datetime timezone to different timezones.
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow) # Output -> 2026-08-29 18:26:14.545060+00:00
dt_ist = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ist) # Output -> 2026-08-30 00:04:00.955693+05:30

# Will print list of available timezones in pytz
for tz in pytz.all_timezones:
    print(tz)

# converting naive to aware time zone ->
dt_mtn = datetime.datetime.now() # Store current time in dt_mtn without timezone
mtn_tz = pytz.timezone('US/Mountain') # Passing a timezone offset to variable named mtn_tz
dt_mtn = mtn_tz.localize(dt_mtn) # Updating dt_mtn by applying mtn_tz timezone offset to dt_mtn datetime
print(dt_mtn) # Output -> 2026-08-30 00:22:03.031511-06:00
# Now it is time zone aware.

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# pytz gotcha: passing tzinfo=pytz.timezone('some_zone') directly into the datetime.datetime() constructor is only safe for UTC. 
# For any DST-observing zone (like 'US/Mountain', 'Asia/Kolkata' doesn't observe DST but others do), 
# this can silently produce the WRONG UTC offset.
# That's why later in this file we correctly use mtn_tz.localize(dt_mtn) instead —
# always use .localize() (for naive→aware) when working with pytz and non-UTC zones.

# Some more useful stuff ->

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain')) # Timezone aware datetime
print(dt_mtn.isoformat()) # Output -> 2026-08-29T12:59:32.204280-06:00
# isoformat -> Standard: It follows ISO 8601, the international standard for representing dates and times.
#              Structure: The standard order goes from largest to smallest unit: YYYY-MM-DDTHH:MM:SS.
#              Separator: The letter "T" separates the date portion from the time portion.

# Using format code to represent datetime in desidred format.
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain')) # Timezone aware datetime
print(dt_mtn.strftime('%B %d, %Y')) # Output -> August 29, 2026
# %B -> Month_name | %d -> two_digit_Day | %Y -> Year
# Got this from python documentation

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# strptime(stringformat_datetime, 'Format in which that string_datetime is')
print(dt) # Output -> 2016-07-26 00:00:00

# strftime -> Datetime to String
# strptime -> String to Datetime   
