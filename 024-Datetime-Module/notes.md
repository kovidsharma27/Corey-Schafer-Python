# Video 24 — Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones

## Status
✅ Completed

## What I Learned
- Learned the difference between naive and aware datetimes.
- Learned how to create and work with dates, times, and datetimes.
- Learned how to calculate date/time differences using timedelta.
- Learned how to get current date, time, and UTC time.
- Learned how to work with timezones using pytz.
- Learned how to format and parse datetime strings.

## What I Practiced
- Used `datetime.date()`, `datetime.time()`, and `datetime.datetime()`.
- Got current date/time using `today()` and `now()`.
- Calculated date differences using `datetime.timedelta()`.
- Converted UTC time to other timezones using `astimezone()`.
- Converted naive datetime to aware datetime using `pytz.timezone().localize()`.
- Formatted datetime to string using `strftime()`.
- Parsed string to datetime using `strptime()`.

## Main Concepts

### Naive vs Aware Datetime
- **Naive** → No timezone info. Simple but can cause confusion across timezones.
- **Aware** → Contains timezone info (offset + DST awareness). Use when timezone accuracy matters.

### `datetime` Module
```python
import datetime
```

### Timedelta
`timedelta` represents a duration (not a specific date) — used to shift dates/times forward or backward.
- Can use days, hours, minutes, seconds, weeks, microseconds, milliseconds.
- Cannot use months or years directly (their lengths vary).

### Timezones (pytz)
```python
import pytz
```
- `pytz.UTC` → safe to pass directly into `tzinfo=`.
- For any other timezone, avoid passing `tzinfo=pytz.timezone(...)` directly — it can produce the wrong offset for DST zones. Use `.localize()` instead for naive → aware conversion.

## Important Commands / Examples

### Date
- `datetime.date(y, m, d)` → Create a specific date.
- `datetime.date.today()` → Today's date.
- `.year`, `.month`, `.day` → Access date parts.
- `.weekday()` → Monday=0 ... Sunday=6.
- `.isoweekday()` → Monday=1 ... Sunday=7.

### Timedelta
- `datetime.timedelta(days=7)` → Creates a 7-day duration.
- `date + timedelta` → Gives a new date.
- `date1 - date2` → Gives a timedelta.
- `.days`, `.total_seconds()` → Access timedelta parts.

### Time
- `datetime.time(h, m, s, micro)` → Create a specific time.
- `.hour`, `.minute`, `.second`, `.microsecond` → Access time parts.

### Datetime
- `datetime.datetime(y, m, d, h, m, s, micro)` → Create date + time.
- `.date()`, `.time()` → Extract date or time portion.
- `datetime.datetime.today()` → Current datetime (no timezone option).
- `datetime.datetime.now()` → Current datetime (accepts optional timezone).
- `datetime.datetime.now(datetime.UTC)` → Current UTC time, **timezone-aware**.
- `datetime.datetime.utcnow()` → Deprecated; gives UTC time but **naive** (no tzinfo).

### Timezones (pytz)
- `pytz.UTC` → UTC timezone object.
- `datetime.datetime.now(tz=pytz.UTC)` → Current aware UTC time.
- `dt.astimezone(pytz.timezone('Zone/Name'))` → Convert aware datetime to another timezone.
- `pytz.timezone('Zone/Name').localize(naive_dt)` → Convert naive datetime to aware (DST-safe).
- `pytz.all_timezones` → List of all available timezone names.

### Formatting
- `dt.isoformat()` → Standard ISO 8601 format (`YYYY-MM-DDTHH:MM:SS`).
- `dt.strftime('%B %d, %Y')` → Datetime → String (e.g., `August 29, 2026`).
- `datetime.datetime.strptime(string, format)` → String → Datetime.

## Practical Example
```python
import datetime
import pytz

# Days until a future date
tday = datetime.date.today()
target = datetime.date(2026, 10, 25)
print((target - tday).days)

# Timezone-aware current time in India
dt_ist = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ist.strftime('%B %d, %Y %I:%M %p'))
```
This calculates days remaining until a target date, then prints the current time in IST in a readable format.

## Verification
I followed the examples from the video and practiced the `datetime` and `pytz` modules.

- `datetime.datetime.utcnow()` is deprecated — use `datetime.datetime.now(datetime.UTC)` instead.
- `timedelta` cannot represent months/years due to variable length.
- Passing `tzinfo=pytz.timezone(...)` directly is only safe for UTC — non-UTC zones need `.localize()` to avoid incorrect DST offsets.

## Notes
- `datetime.date()` → Work with dates.
- `datetime.time()` → Work with time.
- `datetime.datetime()` → Work with date + time.
- `datetime.timedelta()` → Represent a duration.
- `pytz.UTC` → UTC timezone.
- `pytz.timezone().localize()` → Naive → Aware (DST-safe).
- `astimezone()` → Convert between timezones.
- `strftime()` → Datetime → String.
- `strptime()` → String → Datetime.

## Key Takeaway
The `datetime` module handles dates, times, and durations, while `pytz` adds reliable, DST-safe timezone support — together they let Python represent time accurately across the globe.
