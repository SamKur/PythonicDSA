from datetime import datetime, timedelta, date


# Current date and time
now = datetime.now()
print(now)  # e.g., 2024-12-21 10:00:00.123456

# Current date only
today = date.today()
print(today)  # e.g., 2024-12-21

# Format date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # e.g., 2024-12-21 10:00:00

# OR Directly Format Date and Time with f-Strings
formatted = f"{now:%Y-%m-%d %H:%M:%S}"
print(formatted)

# Common format codes
# %Y - Year with century (e.g., 2024)
# %y - Year without century (e.g., 24)
# %m - Month (01-12)
# %d - Day of the month (01-31)
# %H - Hour (00-23)
# %I - Hour (00-12) # in case of AM_PM
# %M - Minute (00-59)
# %S - Second (00-59)
# %p - AM/PM.



# Parsing Strings to Datetime
date_string = "2024-12-21 10:00:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # datetime.datetime(2024, 12, 21, 10, 0)


# Date Arithmetic
# Add 7 days
future_date = today + timedelta(days=7)
print(future_date)  # 2024-12-28
# Subtract 3 hours
three_hours_ago = now - timedelta(hours=3)
print(three_hours_ago)

# ISO format (YYYY-MM-DDTHH:MM:SS)
iso_format = now.isoformat()
print(iso_format)  # e.g., 2024-12-21T10:00:00.123456

# Handling Unix Timestamps
# Convert datetime to timestamp
timestamp = now.timestamp()
print(timestamp)  # e.g., 1703145600.0

# Convert timestamp to datetime
from_timestamp = datetime.fromtimestamp(timestamp)
print(from_timestamp)
