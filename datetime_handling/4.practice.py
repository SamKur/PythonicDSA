# Import Core Built-in Libraries
from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+ (timezone handling)
import time as tm  # For timestamps and sleep



# Best Practices - Always Work with Timezone-Aware Datetimes
dt = datetime(2023, 10, 6, 12, 30, tzinfo=ZoneInfo("Asia/Kolkata"))
print(dt)  # 2023-10-06 12:30:00+05:30



# Use ISO 8601 for Storage and Communication - human-readable and unambiguous.

# Convert datetime to ISO format
iso_str = dt.isoformat()
print(iso_str)  # "2023-10-06T12:30:00+05:30"

# Parse ISO string back to datetime
parsed_dt = datetime.fromisoformat(iso_str)



# Get UNIX timestamp - for precise calculations and comparisons. 

# Always pair with timezone info to avoid ambiguity.
timestamp = dt.timestamp()
print(timestamp)  # 1696581000.0

# Convert timestamp back to datetime
dt_from_ts = datetime.fromtimestamp(timestamp, tz=ZoneInfo("Asia/Kolkata"))



# Use timedelta for adding/subtracting time. (Between datetime objs -> + raises TypeError but - gives timedelta obj)

# Add 1 day, 2 hours
new_dt = dt + timedelta(days=1, hours=2)
print(new_dt)  # 2023-10-07 14:30:00+05:30

# Calculate difference between two datetimes

diff = new_dt - dt
print(diff.total_seconds())  # 93600.0 (seconds)



# Formatting and Parsing

# Format datetime
formatted = dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")
print(formatted)  # "2023-10-06 12:30:00 IST+0530"

# Parse string to datetime
parsed = datetime.strptime("2023-10-06 12:30:00", "%Y-%m-%d %H:%M:%S")
parsed = parsed.replace(tzinfo=ZoneInfo("Asia/Kolkata"))  # Add timezone



# Dealing with Current Time - Always use timezone-aware current time.

# Get current time in a specific timezone
now = datetime.now(ZoneInfo("UTC"))
print(now)  # 2023-10-06 07:00:00+00:00

# Handling Timezones
# Convert to another timezone
ny_time = dt.astimezone(ZoneInfo("America/New_York"))
print(ny_time)  # 2023-10-06 03:00:00-04:00



# Extracting Components

print(dt.year)   # 2023
print(dt.month)  # 10
print(dt.day)    # 6
print(dt.hour)   # 12

